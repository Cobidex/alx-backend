#!/usr/bin/env python3
'''
emulate the behaviour of a simple loggin
'''
from flask import Flask, render_template, g, request
from typing import Optional

app = Flask(__name__)
app.url_map.strict_slashes = False

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
    user_id = request.args.get("login_as", type=int)
    g.user = get_user(user_id)


@app.route('/')
def index():
    '''
    default route
    '''
    return render_template('5-index.html')


if __name__ == '__main__':
    app.run()
