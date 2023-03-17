from flask import Flask
from {{name}}.ext import configuration
from .views import root


def create_app() -> Flask:
    """Create the Flask app and returns it.

    Returns:
        Flask: a Flask app dynamically configured by settings.toml file.
    """
    app = Flask(__name__)
    configuration.init_app(app)

    app.add_url_rule('/', view_func=root)

    return app
