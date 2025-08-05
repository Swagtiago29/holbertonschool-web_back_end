#!/usr/bin/env python3
from flask import Flask, jsonify
from auth import Auth

AUTH = Auth()
app = Flask(__name__)


@app.route('/', methods=['GET'])
def welcome():
    return jsonify({"message": "Bienvenue"})

@app.route('/users', methods=['POST'])
def users(email, password):
    try:
        AUTH.register_user(email, password)
        return {"message": "email already registered"}, 404
    except:
        return {"email": "<registered email>", "message": "user created"}, 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
