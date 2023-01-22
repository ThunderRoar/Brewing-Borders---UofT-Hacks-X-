from flask import Flask, request, render_template
from cohesion import *

app = Flask(__name__)
the_data = []

@app.route("/", methods = ['GET','POST'])
def hello_world():
  if request.method == "POST":
    print (request.form.get("str"))
    the_data.append(request.form.get("str"))
    print(the_data)

  return render_template("Main.html")

@app.route("/page")
def page2():
    return render_template("Page2.html", data = the_data)

print(the_data)


all_data = [ "https://www.coffeedesk.com/blog/wp-content/uploads/2020/05/organic-herbata-zaparzona-1920x1280.jpg",  "fuk no" , "hot",  "no" ,  "no" ,  "no", "https://www.coffeedesk.com/blog/wp-content/uploads/2020/05/organic-herbata-zaparzona-1920x1280.jpg"]
@app.route("/new")
def demo():
    return render_template("Search.html", data = all_data )