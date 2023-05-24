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
    return users.get(user_id)


@app.before_request
def before_request():
    user_id = request.args.get("login_as", type=int)
    g.user = get_user(user_id)


@app.route('/')
def index():
    return render_template('5-index.html')


if __name__ == '__main__':
    app.run()
