#!/usr/bin/python3
"""
starts a Flask web web_flask
"""

from flask import render_template
from flask import Flask
web_flask = Flask(__name__)


@web_flask.route('/', strict_slashes=False)
def hello():
    """hello method"""
    return 'Hello HBNB!'


@web_flask.route('/hbnb', strict_slashes=False)
def hbnb():
    """display method"""
    return 'HBNB'


@web_flask.route('/c/<text>', strict_slashes=False)
def display_var(text):
    """display variable"""
    return 'C %s' % text.replace("_", " ")


@web_flask.route('/python', strict_slashes=False)
@web_flask.route('/python/<text>', strict_slashes=False)
def display_bydefault(text="is cool"):
    """display variable by default"""
    return 'Python %s' % text.replace("_", " ")


@web_flask.route('/number/<int:n>', strict_slashes=False)
def display_int(n):
    """display variable int"""
    return '%d is a number' % n


@web_flask.route('/number_template/<int:n>', strict_slashes=False)
def render_html(n):
    """rendering html"""
    return render_template('5-number.html', n=n)


if __name__ == "__main__":
    web_flask.run(host='0.0.0.0', port=5000)
