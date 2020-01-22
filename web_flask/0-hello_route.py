#!/usr/bin/python3
<<<<<<< HEAD
"""Starts a Flask web application.

The application listens on 0.0.0.0, port 5000.
Routes:
    /: Displays 'Hello HBNB!'
"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """Displays 'Hello HBNB!'"""
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(host="0.0.0.0")
=======
""" Starts a Flask web application """
from flask import Flask


app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello(self):
    """ Displays Greeting HBNB! """
    return ("Hello HBNB!")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
>>>>>>> 677827310ff0f8bbc63da502b7de25208d3ba9ec
