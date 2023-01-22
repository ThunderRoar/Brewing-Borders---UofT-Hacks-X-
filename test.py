from flask import Flask
from cohesion import *

app = Flask(__name__)

@app.route("/")
def hello_world():
    return""" <html>
  <head>
    <link rel="stylesheet" href="https://pyscript.net/latest/pyscript.css" />
    <script defer src="https://pyscript.net/latest/pyscript.js"></script>

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
      <h1>
        How Do You Feel?
      </h1>
    
      
      <input type="search" id="site-search" name="q">  
      <button onclick="window.location.href = 'http://127.0.0.1:5000/page';"> Spill the Tea </button>
      
    </header>

      <div>

      <h2>Today's Beverage</h2>
      <img src="data:image/jpeg;base64,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" alt="tea"
      width=400px 
      height=250px 
      padding: 20px;
      style="border: 0px solid #9AAE88";
      />
      </div>
  </body>
</html>"""

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

