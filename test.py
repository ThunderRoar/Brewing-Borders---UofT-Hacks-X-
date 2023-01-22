from flask import Flask, request, render_template
from cohesion import *

app = Flask(__name__)


@app.route("/")
def hello_world():
    return render_template("Main.html")

@app.route("/page")
def page2():
    return render_template("Page2.html")