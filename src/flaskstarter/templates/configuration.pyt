import os
from importlib import import_module
from dynaconf import FlaskDynaconf

def load_extensions(app):
    for extension in app.config.get('EXTENSIONS'):
        mod = import_module(extension)
        mod.init_app(app)

def init_app(app):
    FlaskDynaconf(app, settings_files=[os.path.join(app.instance_path, 'settings.toml')])
    load_extensions(app)
