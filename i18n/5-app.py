#!/usr/bin/env python3
"""Doc for a small flask app for i18n project"""
from flask import Flask, render_template, request, g
from flask_babel import Babel


class Config:
    """class containing Connfig data"""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)


def get_locale():
    """retuens the best match for our languages"""
    locale = request.args.get('locale')
    if locale in Config.LANGUAGES:
        return locale
    return request.accept_languages.best_match(Config.LANGUAGES)


babel = Babel(app)
babel.init_app(app, locale_selector=get_locale)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user():
    """Return a user dict based on `login_as` URL parameter, or None."""
    login_as = request.args.get('login_as')
    try:
        user_id = int(login_as)
    except (TypeError, ValueError):
        return None
    return users.get(user_id)


@app.before_request
def before_request():
    """Executed before every request. Sets `g.user`."""
    g.user = get_user()


@app.route("/", methods=["GET"])
def index():
    """Function to return template on route=/ """
    return render_template("5-index.html", get_locale=get_locale())


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
