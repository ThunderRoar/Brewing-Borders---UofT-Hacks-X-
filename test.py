from flask import Flask, request, render_template
from cohesion import *

app = Flask(__name__)



@app.route("/")
def hello_world():
    return render_template("Main.html")

@app.route("/page")
def page2():
    return """<html>
    <head>
      <link rel="stylesheet" href="https://pyscript.net/latest/pyscript.css" />
      <script defer src="https://pyscript.net/latest/pyscript.js"></script>
    </head>
    
<head>
    <title>Brewing Borders</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>

<style>
  h1 {text-align: center;}
  p {text-align: center;}
  div {text-align: center;}

    /* Style the header */
    header {
      background-color: #F5E5D6;
      padding: 30px;
      text-align: center;
      font-size: 35px;
      color: rgb(0, 0, 0);
    }

    
  img {
    border-radius: 120px 20px 120px 20px;    }

    div{
      background-color: #9AAE88;
      padding: 20px;
      text-align: center;
      font-size: 35px;
      color: rgb(0, 0, 0);
    }

    @font-face { font-family: Cuprum; src: url('Cuprum-Regular.ttf'); } 

    h1{
      font-family: Cuprum, sans-serif;
    }
    h2{
      font-family: Cuprum, sans-serif;
    }

</style>


<body>
  <header>

    <button onclick="window.location.href = 'http://127.0.0.1:5000';"> Home </button>

    <h1>
      Recommendation
    </h1>
  </header>


 
    <div>

    <h2>Mad Amounts of Alcohol</h2>
    <img src=https://toronto-alcohol-delivery.ca/wp-content/uploads/2020/07/baccardi-gold-600x800.png alt="toxic"
    width=250px 
    height=350px 
    padding: 20px;
    />


    </div>

</body>

</html>"""

