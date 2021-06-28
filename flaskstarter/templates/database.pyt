import os
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from typing import NoReturn
from flask import Flask

db = SQLAlchemy()
migrate = Migrate()

def init_app(app : Flask) -> NoReturn:
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(app.instance_path,'{{name}}.db')
    db.init_app(app)
    migrate.init_app(app, db)