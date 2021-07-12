import os
from sqlalchemy import MetaData
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from typing import NoReturn
from flask import Flask

db = SQLAlchemy()
migrate = Migrate()

convention = {
    "ix": 'ix_%(column_0_label)s',
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
}


def init_app(app : Flask) -> NoReturn:
    metadata = MetaData(naming_convention=convention)
    db.init_app(app, metadata=metadata)
    migrate.init_app(app, db)
