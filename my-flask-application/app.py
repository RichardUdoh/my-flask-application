# app.py
import requests

from flask import Flask, request
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route('/elapsed/', methods=["POST"])
def get_elapsed():
    req_data = request.get_json()
    website = req_data["url"]
    d = dict()
    d[website] = requests.get(website).elapsed.total_seconds()
    return d    

 