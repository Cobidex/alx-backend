#!/usr/bin/env python3
'''
emulate the behaviour of a simple loggin
'''
from flask import Flask, render_template, g, request
from typing import Optional
from flask_babel import Babel

app = Flask(__name__)
app.url_map.strict_slashes = False
babel = Babel(app)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user(user_id: int) -> Optional[dict]:
    '''
    get user info
    '''
    return users.get(user_id)


@app.before_request
def before_request():
    '''
    set user to user info
    '''
    user_id: int = request.args.get("login_as")
    g.user: dict = get_user(user_id)


@babel.localeselector
def get_locale():
    '''
    gets the locale of the user
    '''
    locale = requests.args.get('locale')

    if locale and locale in app.config['LANGUAGES']:
        return locale
    return requests.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    '''
    default route
    '''
    return render_template('5-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
