#!/usr/bin/python3
"""
Flask web application
"""

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """return"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """return"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def cisfun(text):
    """display C <text> """
    return ("C %s" % text.replace('_', ' '))


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text='is cool'):
    """display by case of path"""
    return ("Python %s" % text.replace('_', ' '))


@app.route('/number/<int:n>', strict_slashes=False)
def isnumber(n):
    """ display n if is an integer"""
    return ("%d is a number" % n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
