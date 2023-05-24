#!/usr/bin/env python3

"""
This is a basic Flask app that displays a welcome message.
"""

from flask import Flask, render_template
from flask_babel import Babel, gettext

app = Flask(__name__)
babel = Babel(app)


class Config(object):
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
    welcome_title = gettext('Hello world')
    welcome_header = gettext('Welcome to holberton')
    return render_template('1-index.html', welcome_title=welcome_title,
                           welcome_header=welcome_header)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
