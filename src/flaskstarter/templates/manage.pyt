"""Copyright 2021 Felipe Bastos Nunes

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
"""
import click
import os
import subprocess
from string import Template

@click.group()
def manage():
    '''This script manages the {{name}} project.'''

@manage.command()
@click.argument('port', default='5000')
def runserver(port):
    '''Run Flask server on development mode and selected TCP port.'''
    cmd = ''
    if os.name == 'posix':
        cmd = f'. .venv/bin/activate; export FLASK_APP={{name}}; export FLASK_ENV=development; flask run --port={port}'
    elif os.name == 'nt':
        cmd = f'call .venv/Scripts/activate; set FLASK_APP={{name}}; set FLASK_ENV=development; flask run --port={port}'
    subprocess.run(cmd, shell=True)

@manage.command()
@click.argument('name')
def create_blueprint(name : str):
    '''Creates but does not add to init a blueprint file.'''
    os.mkdir(os.path.join(os.getcwd(), '{{name}}', name))
    blueprint = open(os.path.join(os.getcwd(), '{{name}}', 'blueprints', f'{name}.py'), 'w')
    blueprint_string = "from flask import Blueprint\n\nbp = Blueprint('$name', __name__, url_prefix='/$name')\n@bp.route('/')\ndef root():\n    return 'Hello from $name'\ndef init_app(app):\n    app.register_blueprint(bp)"
    bluet = Template(blueprint_string)
    blueprint.write(bluet.substitute(name=name))
    blueprint.close()
    click.echo('Blueprint created. Remember to add it to your application on instance/settings.toml.')

if __name__ == '__main__':
    manage(prog_name='manage')
