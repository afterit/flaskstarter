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
from typing import final
import click
import os
import subprocess

from jinja2 import Environment, PackageLoader, select_autoescape

from flaskstarter.tools.requirements import add_support_to, install_requirements


def print_version(ctx, param, value):
    if not value or ctx.resilient_parsing:
        return
    click.echo('flaskstarter 0.2')
    ctx.exit()


@click.group()
@click.option('--version', is_flag=True, default=False, callback=print_version,
              expose_value=False, is_eager=True)
def flaskstarter():
    """A program to start a Flask project under a modular structure.
    """


@flaskstarter.command()
@click.argument('name')
@click.option('-l', '--login', is_flag=True, default=False, help='Adds flask-login.')
@click.option('-a', '--alchemy', is_flag=True, default=False, help='Adds flask-sqlalchemy.')
@click.option('-b', '--bcrypt', is_flag=True, default=False, help='Adds flask-bcrypt.')
@click.option('-w', '--wtforms', is_flag=True, default=False, help='Adds flask-wtform.')
def init(name : str, login : bool, alchemy : str, bcrypt : str, wtforms : str):
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
    os.makedirs(os.path.join(os.getcwd(), name, 'instance', 'uploads'))
    click.echo('Done!')

    click.echo('Creating first python scripts... ')
    env = Environment(
        loader=PackageLoader('flaskstarter', 'templates'),
        autoescape=select_autoescape('pyt', 'sht', 'batt')
    )

    initpy = open(os.path.join(os.getcwd(), name, name, '__init__.py'), 'w')    
    initpyt = env.get_template('init.pyt')
    initpy.write(initpyt.render(name=name, flaskbcrypt=bcrypt, flasksqlalchemy=alchemy, flasklogin=login))
    initpy.close()
    
    routespy = open(os.path.join(os.getcwd(), name, name, 'routes.py'), 'w')
    routespyt = env.get_template('routes.pyt')
    routespy.write(routespyt.render(name=name, login=login, db=alchemy))
    routespy.close()

    if login and alchemy:
        entitiespy = open(os.path.join(os.getcwd(), name, name, 'entities.py'), 'w')
        entitiespyt = env.get_template('entities.pyt')
        entitiespy.write(entitiespyt.render(name=name))
        entitiespy.close()

    click.echo('Done!')

    index = open(os.path.join(os.getcwd(), name, name, 'templates', 'index.html'), 'w')
    indext = env.get_template('index.htmlt')
    index.write(indext.render(name=name))
    index.close()

    # Clonning your own virtualenv
    click.echo("ATTENTION: if this next stage fails, you should check if you do have venv on your system's Python.")
    click.echo('Clonning python onto its own virtual enviroment... ')
    subprocess.run(f'python3 -m venv {os.path.join(os.getcwd(), name, ".venv")}', shell=True)
    click.echo('Done!')

    # Requirements will help you do the basic startup of your virtualenv.
    add_support_to(True, name, 'flask')
    add_support_to(login, name, 'flask-login')
    add_support_to(alchemy, name, 'flask-sqlalchemy')
    add_support_to(bcrypt, name, 'flask-bcrypt')
    add_support_to(wtforms, name, 'flask-wtf')
    click.echo('If you do have other requirements, feel free to customize it.')

    # Creating some helpful scripts.
    click.echo('I will create a management script for running the project.')
    manage = open(os.path.join(os.getcwd(), name, 'manage.py'), 'w')
    managet = env.get_template('manage.pyt')
    manage.write(managet.render(name=name))
    manage.close()
    click.echo('manage.py script created. Feel free to customize it.')

    #Requirements installing.
    click.echo('I will install the requirements for you.')
    install_requirements(name)
    click.echo('Done!')

    return 0


if __name__ == '__main__':
    flaskstarter(prog_name='flaskstarter')
