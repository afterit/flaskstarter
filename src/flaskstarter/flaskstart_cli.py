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

@click.group()
def flaskstarter():
    """A program to start a Flask project under a modular structure.
    """

@flaskstarter.command()
@click.argument('name')
@click.option('-l', '--login', prompt="Will you use Flask-Login? [yes/no]", default='no', help='Adds flask-login')
@click.option('-a', '--alchemy', prompt="Will you use Flask-SQLAlchemy? [yes/no]", default='no', help='Adds flask-sqlalchemy')
@click.option('-b', '--bcrypt', prompt="Will you use Flask-Bcrypt? [yes/no]", default='no', help='Adds flask-bcrypt')
@click.option('-w', '--wtforms', prompt="Will you use Flask-WTForm? [yes/no]", default='no', help='Adds flask-wtform')
def init(name : str, login : str, alchemy : str, bcrypt : str, wtforms : str):
    """Creates the project directory tree under the name provided."""
    # All directories and basic python files are created here
    click.echo('Creating project tree... ')
    try:
        os.mkdir(os.path.join(os.getcwd(), name))
    except FileExistsError:
        click.echo(f'Project with name "{name}" already exists. Exiting.')
        exit(0)
    os.makedirs(os.path.join(os.getcwd(), name, name, 'templates'))
    os.makedirs(os.path.join(os.getcwd(), name, name, 'static'))
    os.mkdir(os.path.join(os.getcwd(), name, '.venv'))
    click.echo('Done!')

    click.echo('Creating first python scripts... ')
    initpy = open(os.path.join(os.getcwd(), name, name, '__init__.py'), 'w')
    initpy.write(f'# This file is part of {name} project.{os.linesep}from flask import Flask{os.linesep}')
    initpy.write(f'def create_app():{os.linesep}    app = Flask("__name__"){os.linesep}')
    initpy.write(f'    with app.app_context():{os.linesep}')
    initpy.write(f'        from . import routes{os.linesep}')
    initpy.write(f'    return app{os.linesep}')
    initpy.close()

    routespy = open(os.path.join(os.getcwd(), name, name, 'routes.py'), 'w')
    routespy.write(f'# This file is part of {name} project.{os.linesep}from flask import current_app as app{os.linesep}')
    routespy.write(f'@app.route("/"){os.linesep}')
    routespy.write(f'def root():{os.linesep}')
    routespy.write(f'    return "Hello, from Flask!"{os.linesep}')
    routespy.close()
    click.echo('Done!')

    # Clonning your own virtualenv
    click.echo("ATTENTION: if this next stage fails, you should check if you do have venv on your system's Python.")
    click.echo('Clonning python onto its own virtual enviroment... ')
    subprocess.run(f'python3 -m venv {os.path.join(os.getcwd(), name, ".venv")}', shell=True)
    click.echo('Done!')

    # Requirements will help you do the basic startup of your virtualenv.
    requirements = open(os.path.join(os.getcwd(), name, 'requirements.txt'), 'w')
    add_support_to('yes', requirements, 'flask')
    add_support_to(login, requirements, 'flask-login')
    add_support_to(alchemy, requirements, 'flask-sqlalchemy')
    add_support_to(bcrypt, requirements, 'flask-bcrypt')
    add_support_to(wtforms, requirements, 'flask-wtf')
    requirements.close()
    click.echo('If you do have other requirements, feel free to customize it.')

    # Creating some helpful scripts.
    click.echo('I will create some helpful scripts for running the project.')
    runsh = open(os.path.join(os.getcwd(), name, 'run.sh'), 'w')
    runsh.write(f'#!/bin/bash{os.linesep}')
    runsh.write(f'. .venv/bin/activate{os.linesep}')
    runsh.write(f'export FLASK_APP={name}{os.linesep}')
    runsh.write(f'export FLASK_ENV=development{os.linesep}')
    runsh.write(f'flask run{os.linesep}')
    runsh.close()
    if os.name == 'posix':
        subprocess.run(f'chmod +x {os.path.join(os.getcwd(), name, "run.sh")}', shell=True)

    runbat = open(os.path.join(os.getcwd(), name, 'run.bat'), 'w')
    runbat.write(f'call .venv\Scripts\activate{os.linesep}')
    runbat.write(f'set FLASK_APP={name}{os.linesep}')
    runbat.write(f'set FLASK_ENV=development{os.linesep}')
    runbat.write(f'flask run{os.linesep}')
    runbat.close()
    click.echo('Scripts created. Feel free to customize it.')

    #Requirements installing.
    if os.name == 'posix':
        click.echo('I will install the requirements for you.')
        cmd = f'. {os.path.join(os.getcwd(), name, ".venv", "bin", "activate")}; pip install -r {os.path.join(os.getcwd(), name, "requirements.txt")};'
        subprocess.call(cmd, shell=True)
        click.echo('Done!')
    elif os.name == 'nt':
        temp = open(os.path.join(os.getcwd(), name, 'temp.bat'), 'w')
        temp.write(f'call .venv/bin/activate{os.linesep}')
        temp.write(f'pip install -r requirements.txt')
        temp.close()
        subprocess.run(os.path.join(os.getcwd(), name, 'temp.bat'), shell=True)

    return 0


def add_support_to(add, file, module):
    if add == 'yes':
        click.echo(f'Adding {module} support... ')
        file.write(f'{module}{os.linesep}')
        click.echo('Done!')
    elif add == 'no':
        click.echo(f'Skipping {module}')
    else:
        click.echo(f'Option "{add}" unrecognized for {module}.')
        exit(0)


if __name__ == '__main__':
    flaskstarter(prog_name='flaskstarter')
