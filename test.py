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
