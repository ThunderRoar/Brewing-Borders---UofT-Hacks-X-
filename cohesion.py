import cohere
import csv
api_key = '4PguL5I35AkrSLLRhDNpfXRkX2YiVFDy7uJtQNeT'
co = cohere.Client(api_key)
from cohere.classify import Example
issue = r'issues_and_situations.csv'

def read_csv(csv_name):
    with open(csv_name, encoding="utf8") as f:
        csv_reader = csv.reader(f)
        statement = []
        result = []
        for line in csv_reader:
            statement.append(line[0])
            result.append(line[1])
        return (statement, result)

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