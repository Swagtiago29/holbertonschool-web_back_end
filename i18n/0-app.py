#!/usr/bin/env python3
from flask import flask, render_template

app = flask(__name__)


@app.route("/", methods=["GET"])
def hello():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
