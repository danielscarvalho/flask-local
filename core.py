# A simple Flask Hello World WEB API to get started with...

from flask import Flask
from flask import request
from datetime import datetime
import insperds

app = Flask(__name__)

@app.route('/')
def hello_world():
    now = datetime.now()
    return 'Hello from Flask, by Insper DS! - ' + str(now)

@app.route('/core')
def core():
    now = datetime.now()
    return 'Vai Corinthians!! - ' + str(now) 

@app.route('/add/<a>/<b>')
def add(a, b):
    a_float=0
    b_float=0

    try:
       a_float = float(a)
    except:
       return "Ops! Not a float: " + a
    
    try:
       b_float = float(b)
    except:
       return "Ops! Not a float: " + b
    
    return str(a_float + b_float)

@app.route('/area')
def myarea():
  altura = request.args.get('altura', default = 0, type = float)
  largura = request.args.get('largura', default = 0, type = float)
  comprimento = request.args.get('comprimento', default = -1, type = float)
  
  if (comprimento < 0):
        return str(altura*largura)
  else:
        return str(altura*largura*comprimento)

@app.route('/query/<text>')
def query(text):
    return insperds.ddgquery(text)
    
@app.route('/bitcoins')
def btc():
    return insperds.bitcoins()
    
@app.route('/ethereum')
def ether():
    return insperds.ethereum()
    
@app.route('/weather/<lat>/<lon>')
def weather(lat, lon):
    return insperds.weather(lat, lon)
            
