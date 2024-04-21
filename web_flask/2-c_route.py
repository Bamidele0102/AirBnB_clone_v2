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
app.url_map.strict_slashes = False


@app.route('/')
def hello_hbnb():
    """Function that displays "Hello HBNB!"""
    return "Hello HBNB!"


@app.route('/hbnb')
def hbnb():
    """Function that displays "HBNB!"""
    return "HBNB!"


@app.route('/c<text>')
def c_text(text):
    """Function that displays custom text given by user"""
    return "C".format(text.replace('_', ' '))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
