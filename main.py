#!/usr/bin/env python3

import requests
import json
from flask import Flask
from functools import wraps

def get_ip():
	endpoint = 'https://ipinfo.io/json'
	response = requests.get(endpoint, verify = True)
	if response.status_code != 200:
		return 'Status:', response.status_code, 'Problem with the request. Exiting.'
		exit()
	data = response.json()
	return data['ip']

#get my ip
my_ip = get_ip()

app = Flask(__name__)
def multiline(fn):
	@wraps(fn)
	def _fn(*args, **kwargs):
		return "<xmp>" + fn(*args, **kwargs) + "</xmp>"
	return _fn

@app.route("/")
@multiline
def index():
	return "IP: " + my_ip

if __name__ == "__main__":
	app.run(host="0.0.0.0", port=8080, debug=True)