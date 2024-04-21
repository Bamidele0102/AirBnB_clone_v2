#!/usr/bin/python3
"""
Start a Flask web app that listen on 0.0.0.0, port 5000
routes: /: display "Hello HBNB!"
routes: /hbnb: display "HBNB!"
routes: /c/<text>: display “C ” followed by the value
                    of the text variable (replace underscore _
                    symbols with a space )
routes: /python: display "Python is cool"
routes: /number/<n>
routes: /number_template/<n>: display a HTML page only if n is an intege
"""

from flask import Flask, render_template
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


@app.route('/c/<text>')
def c_text(text):
    """Function that displays custom text given by user"""
    return 'C {}'.format((text.replace('_', ' ')))


@app.route('/python')
@app.route('/python/<text>')
def python_text(text="is cool"):
    """This is for Python route"""
    return 'Python {}'.format(text.replace('_', ' '))


@app.route('/number/<int:n>')
def text_if_int(n):
    """Display text only if int given"""
    return "{:d} is a number".format(n)


@app.route('/number_template/<int:n>')
def template_int(n):
    """Display a HTML page only if n is an integer"""
    return render_template('5-number.html', number=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
