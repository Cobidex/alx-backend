#!/usr/bin/env python3

"""
This is a Flask app that displays a welcome message in the selected language.
"""

from flask import Flask, render_template, request
from flask_babel import Babel, gettext

app = Flask(__name__)
babel = Babel(app)


class Config:
    '''
    configuration class
    '''
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


@babel.localeselector
def get_locale():
    '''
    determine the best match with our supported languages
    '''
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index() -> str:
    '''
    default route
    '''
    welcome_title = gettext('home_title')
    welcome_header = gettext('home_header')
    return render_template('2-index.html',
                           welcome_header=welcome_message
                           welcome_title=welcome_title)


if __name__ == '__main__':
    app.run()
