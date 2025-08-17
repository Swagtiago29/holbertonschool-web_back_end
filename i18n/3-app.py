#!/usr/bin/env python3
"""Doc for a small flask app for i18n project"""
from flask import Flask, render_template, request
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
    return request.accept_languages.best_match(Config.LANGUAGES)


babel = Babel(app)
babel.init_app(app, locale_selector=get_locale)


@app.route("/", methods=["GET"])
def index():
    """Function to return template on route=/ """
    return render_template("3-index.html", get_locale=get_locale())


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
