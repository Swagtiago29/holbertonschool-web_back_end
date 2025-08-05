#!/usr/bin/env python3
from flask import Flask, jsonify, request
from auth import Auth

AUTH = Auth()
app = Flask(__name__)


@app.route('/', methods=['GET'])
def welcome():
    return jsonify({"message": "Bienvenue"})

@app.route('/users', methods=['POST'])
def users():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')
    try:
        AUTH.register_user(email, password)
        return {"email": email, "message": "user created"}, 200
    except ValueError:
        return {"message": "email already registered"}, 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
