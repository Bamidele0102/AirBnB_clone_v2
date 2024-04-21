#!/usr/bin/python3
"""
Start a Flask web app that listen on 0.0.0.0, port 5000
routes: /: display "Hello HBNB!"
routes: /hbnb: display "HBNB!"
routes: /c/<text>: display “C ” followed by the value
                    of the text variable (replace underscore _
                    symbols with a space )
"""

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes = False)
def index():
    """Function that displays "Hello HBNB!"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes = False)
def hbnb():
    """Function that displays "HBNB!"""
    return 'HBNB!'


@app.route('/c<text>', strict_slashes = False)
def c_text(text):
    """Function that displays custom text given by user"""
    return 'C ' + text.replace('_', ' ')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
