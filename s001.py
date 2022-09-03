from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route("/core")
def core():
    now = datetime.now()
    return "<h1>Vai Corinthians!!! - " + str(now) + "</h1>"
    
@app.route("/")
def webroot():
    now = datetime.now()
    return "<h1>Insper DS!!! - " + str(now) + "</h1>"    

