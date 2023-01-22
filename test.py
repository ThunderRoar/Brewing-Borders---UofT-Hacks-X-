from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return """<body>
  <header>
    <h1>How Do You Feel?</h1>
    <div>
    <input type="search" id="site-search" name="q">  
    <button>Spill the Tea</button>
    </div>
  </header>
    <div>
    <h2>Olong Tea</h2>
    <img src="olong.jpg" alt="tea"
    width=50% 
    height=30% 
    padding: 20px;
    border-radius: 50%;
    style="border: 60px solid #9AAE88";
    class="longer-bottom-border"
    />
    </div>
</body>"""