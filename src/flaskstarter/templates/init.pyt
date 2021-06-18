import os

from flask import Flask
from {{name}}.ext import configuration

def create_app():
    app = Flask(__name__, instance_relative_config=True)
    configuration.init_app(app)

    app.config['UPLOAD_FOLDER'] = os.path.join(app.instance_path,'uploads')

    with app.app_context():
        from . import views
    
    return app
