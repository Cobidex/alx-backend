#!/usr/bin/env python3

"""
This is a Flask app that displays a welcome message in the selected language.
"""

from flask import Flask, render_template, request
from flask_babel import Babel, gettext

app = Flask(__name__)
babel = Babel(app)


class Config:
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


@babel.localeselector
def get_locale():
    '''
    gets best matched language
    '''
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    '''
    default route
    '''
    welcome_title = gettext('home_title')
    welcome_header = gettext('home_header')
    return render_template('3-index.html', welcome_title=welcome_title,
                           welcome_header=welcome_header)


if __name__ == '__main__':
    app.run()
