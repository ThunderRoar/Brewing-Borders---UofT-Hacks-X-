from flask import Flask, request, render_template
from cohesion import *
from drinks_backend import *

app = Flask(__name__)
the_data = [' ']

@app.route("/", methods = ['GET','POST'])
def hello_world():
  if request.method == "POST":
    #print (request.form.get("str"))
    the_data.append(request.form.get("str"))
    #print(the_data)

  return render_template("Main.html")

@app.route("/page")
def page2():
    return render_template("Page2.html", data = the_data)





@app.route("/new")
def demo():
  a_list = classify(the_data[-1])

  print(a_list[-1])
  return render_template("Search.html", data = a_list )