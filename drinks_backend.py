import cohere
import csv
import time
import random
import openai
openai.api_key = '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'
from concurrent.futures import ThreadPoolExecutor
api_key = '4PguL5I35AkrSLLRhDNpfXRkX2YiVFDy7uJtQNeT'
map_api = 'f64150a250e943538522123699ace796'
co = cohere.Client(api_key)
from cohere.classify import Example
caffeine = r'/Users/leoliao/Downloads/Data/Caffeine.csv'
temperature = r'/Users/leoliao/Downloads/Data/Temperature.csv'
drinks = r'/Users/leoliao/Downloads/Data/Drinks.csv'
carbonation = r'/Users/leoliao/Downloads/Data/Carbonation.csv'
alcohol = r'/Users/leoliao/Downloads/Data/Alcohol.csv'
countries = r'/Users/leoliao/Downloads/Data/Countries.csv'


def desc(drink):
    prompt = 'Generate a description on the drink: '+drink
    completions = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=1.0,
    )

    message = completions.choices[0].text
    return(message.replace('\n', ' '))

def map(country):
    # read the country csv to find the longitude and lat of a county
    country_list = read_all(countries)[1:]
    long = 0
    lat = 0
    for place in country_list:
        if place[3] == country:
            long = place[1]
            lat = place[2]
    link = r"https://maps.geoapify.com/v1/staticmap?style=osm-liberty&width=600&height=400&center=lonlat:{},{}&zoom=2&marker=lonlat:{},{};color:%23ff0000;size:medium&apiKey={}".format(long, lat, long, lat, map_api)
    return link



def read_csv(csv_name):
    with open(csv_name, encoding="utf8") as f:
        csv_reader = csv.reader(f)
        statement = []
        result = []
        for line in csv_reader:
            statement.append(line[0])
            result.append(line[1])
        return (statement, result)

def read_all(csv_name):
    with open(csv_name, encoding="utf8") as f:
        csv_reader = csv.reader(f)
        result = []
        for line in csv_reader:
            result.append(line)
        return (result)

def predic_confid(returnstr):
    def parse_data(str_to_parse: str, keyword: str):
        LEEWAY = 15
        keyword_indice = str_to_parse.find(keyword) + len(keyword)
        str_to_parse = str_to_parse[keyword_indice:keyword_indice + LEEWAY]
        str_to_parse = str_to_parse[str_to_parse.find('\n')-1::-1]
        # reversing the resultant as we read the string backwards
        resultant = str_to_parse[::-1]
        return resultant


    #isolating the prediction

    prediction = parse_data(returnstr, 'prediction: ')
    #searching for the prediction and its matching confidence level
    str_to_find = (prediction+'\n\tconfidence: 0')
    confidence = parse_data(returnstr, str_to_find)

    return (prediction, confidence)

def generate_examples(csv_name:str, statement_indice: int, result_indice: int):
    training_data = read_csv(csv_name)
    example_list = []
    for i in range (len(training_data[statement_indice])):
        example_list.append(Example(training_data[statement_indice][i],
                                    training_data[result_indice][i]))
    return example_list

#try to classify what issue the user is dealing with
def senti_analysis(str_to_analyse: str, file_name: str):
    examples = generate_examples(file_name, 0, 1)

    inputs = [str_to_analyse]
    response = co.classify(
      model='large',
      inputs=inputs,
      examples=examples)
    return(predic_confid(str(response.classifications)))

def senti_analysis_with_thread(str_to_analyse, file_name):
    return senti_analysis(str_to_analyse, file_name)

# returns a tuple in the form of (drink name, country, caffeine, alcohol, carbonation, temperature, link of img, description)
def find_drink(caffeine, alcohol, carbonation, temperature):
    # in the event that no drink matches all four traits we keep subtracting traits until we find one that works
    # read the lines within the drinks file and turn it into a list of lists
    reco_drinks = []
    drink_list = read_all(drinks)[1:]
    for drink in drink_list:
        if drink[2] == caffeine and drink[3] == alcohol and drink[4] == carbonation and drink[5] == temperature:
            reco_drinks.append(drink)
    if reco_drinks == []:
        for drink in drink_list:
            if drink[2] == caffeine and drink[3] == alcohol and drink[4] == carbonation:
                reco_drinks.append(drink)
    if reco_drinks == []:
        for drink in drink_list:
            if drink[2] == caffeine and drink[3] == alcohol:
                reco_drinks.append(drink)
    if reco_drinks == []:
        for drink in drink_list:
            if drink[3] == alcohol:
                reco_drinks.append(drink)
    indice = random.randint(0, len(reco_drinks)-1)
    description = desc(reco_drinks[indice][0])
    country = map(reco_drinks[indice][0])
    # return the link to the image of the picture
    return (reco_drinks[indice][0], reco_drinks[indice][1], reco_drinks[indice][2], reco_drinks[indice][3], reco_drinks[indice][4], reco_drinks[indice][5], country, description)


def classify(prompt):
    with ThreadPoolExecutor() as executor:
        caff = executor.submit(senti_analysis_with_thread, prompt, caffeine)
        carbon = executor.submit(senti_analysis_with_thread, prompt, carbonation)
        temp = executor.submit(senti_analysis_with_thread, prompt, temperature)
        alco = executor.submit(senti_analysis_with_thread, prompt, alcohol)
    return find_drink(caff.result()[0], alco.result()[0], carbon.result()[0], temp.result()[0])
