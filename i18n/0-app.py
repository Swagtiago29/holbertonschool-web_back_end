#!/usr/bin/env python3
from flask import flask, jsonify

app = flask(__name__)
@app.route("/", methods=["GET"])
def hello():
    return jsonify("hello"), 200
