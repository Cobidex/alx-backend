#!/usr/bin/env python3

"""
This is a basic Flask app that displays a welcome message.
"""

from flask import Flask, render_template
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


class Config:
    '''
    defines configuration variables for flask app
    '''
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


@app.route('/')
def index() -> str:
    '''
    default route
    '''
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run()
