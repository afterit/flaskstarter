import os

from flask import Flask
from {{name}}.ext import configuration

def create_app():
    app = Flask(__name__)
    configuration.init_app(app)

    with app.app_context():
        from . import views
    
    return app
