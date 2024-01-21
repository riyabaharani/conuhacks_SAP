from flask import Flask
import flask
import json
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def hello():
    return "Hello, World!"

@app.route('/users', methods=["GET"])
def users():
    print("users endpoint reached...")
    with open("backend/users.json", "r") as f:
        data = json.load(f)
        return flask.jsonify(data)

if __name__ == "__main__":
    app.run("localhost")