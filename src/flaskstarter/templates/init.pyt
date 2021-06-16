from flask import Flask
import os
{% if flasklogin: %}
from flask_login import LoginManager
{% endif %}
{% if flasksqlalchemy: %}
from flask_sqlalchemy import SQLAlchemy
{% endif %}
{% if flaskbcrypt: %}
from flask_bcrypt import Bcrypt
{% endif %}

{% if flasklogin: %}
login_manager = LoginManager()
{% endif %}
{% if flasksqlalchemy: %}
db = SQLAlchemy()
{% endif %}
{% if flaskbcrypt: %}
bcrypt = Bcrypt()
{% endif %}

def create_app():
    app = Flask(__name__, instance_relative_config=True)

    app.secret_key = os.getenv('SECRET_KEY', default='123456')

    {% if flasksqlalchemy: %}
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(app.instance_path,'{{name}}.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    {% endif %}

    app.config['UPLOAD_FOLDER'] = os.path.join(app.instance_path,'uploads')

    {% if flasklogin: %}
    login_manager.init_app(app)
    {% endif %}
    {% if flasksqlalchemy: %}
    db.init_app(app)
    {% endif %}
    {% if flaskbcrypt: %}
    bcrypt.init_app(app)
    {% endif %}

    with app.app_context():
        from . import routes
    
    return app
