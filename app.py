# -*- coding: utf-8 -*-
"""
@Time ： 2020/3/9 11:12
@Auth ： paul
@File ：app.py
@IDE ：PyCharm
"""
from flask import Flask, render_template, request, jsonify
import requests
import numpy as np
import json

app = Flask(__name__)


def make_request(url, data):
    data = (255.0 - np.array(data)).reshape([1, 28, 28, 1])
    data = {"signature_name": "serving_default", "instances": [{"input_1": data.tolist()[0]}]}
    output = requests.post(url, json=data)
    output = json.loads(output.text)['predictions'][0]
    return output


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/mnist", methods=["post"])
def index1():
    a = make_request("http://localhost:18502/v1/models/lenet:predict", request.json)
    b = make_request("http://localhost.com:18501/v1/models/lenet:predict", request.json)

    return jsonify(results=[a, b])


if __name__ == '__main__':
    app.debug = True
    app.run(port=8000)
