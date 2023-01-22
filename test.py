from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return """<h1>How Do You Feel?</h1>
    <div>
    <input type="search" id="site-search" name="q">  
    <button>Spill the Tea</button>
    </div>"""