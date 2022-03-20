#!/usr/bin/python3
"""Starts a Flask web app"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    '''Display a message'''
    return 'Hello HBNB!'

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    '''Display <HBNB>'''
    return 'HBNB'

@app.route('/c/<text>', strict_slashes=False)
def c(text):
    '''display “C” followed by the value of the text
    variable'''
    return 'C {}'.format(text).replace('_', ' ')

@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text='is cool'):
    '''display "Python + <text>"'''
    return 'Python {}'.format(text).replace('_', ' ')

@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    '''display "<n>" if it's a number'''
    return '{} is a number'.format(n)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
