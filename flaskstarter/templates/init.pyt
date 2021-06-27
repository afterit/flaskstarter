from flask import Flask
from {{name}}.ext import configuration
from .views import root


def create_app():
    app = Flask(__name__, instance_relative_config=True)
    configuration.init_app(app)

    app.config['UPLOAD_FOLDER'] = os.path.join(app.instance_path,'uploads')

    app.add_url_rule('/', view_func=root)

    return app
