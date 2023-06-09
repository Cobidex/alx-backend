#!/usr/bin/env python3

"""
This is a Flask app that displays a welcome message in the selected language.
"""

from flask import Flask, render_template, request
from flask_babel import Babel, gettext

app = Flask(__name__)
babel = Babel(app)


class Config(object):
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
    return render_template('3-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
