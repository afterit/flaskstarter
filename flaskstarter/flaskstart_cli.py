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

from flaskstarter.tools.requirements import add_support_to, install_requirements
from flaskstarter.tools.templating import get_template

def print_version(ctx, param, value):
    """Prints CLI version on 'flaskstarter --version'.

    Explained on Click documentation as a pattern to attend --version.

    Args:
        ctx ([type]): Checks Click's documentation.
        param ([type]): Checks Click's documentation.
        value ([type]): Checks Click's documentation.
    """
    if not value or ctx.resilient_parsing:
        return
    click.echo(f'flaskstarter 0.3')
    ctx.exit()


@click.group()
@click.option('--version', is_flag=True, default=False, callback=print_version,
              expose_value=False, is_eager=True)
def flaskstarter():
    """A program to start a Flask project under a modular structure."""


@flaskstarter.command()
@click.argument('name')
def init(name: str):
    """Creates the project directory tree under the name provided.

    Args:
        name (str): Project's name to create.

    """

    # All directories and basic python files are created here
    click.echo('Creating project tree... ')
    try:
        os.mkdir(os.path.join(os.getcwd(), name))
    except FileExistsError:
        click.echo(f'Project with name "{name}" already exists. Exiting.')
        exit(0)

    os.makedirs(os.path.join(os.getcwd(), name, name, 'ext'))
    ext_is_package = open(os.path.join(
        os.getcwd(), name, name, 'ext', '__init__.py'), 'w')
    ext_is_package.close()
    os.makedirs(os.path.join(os.getcwd(), name, name, 'blueprints'))
    blueprint_is_package = open(os.path.join(
        os.getcwd(), name, name, 'ext', '__init__.py'), 'w')
    blueprint_is_package.close()

    os.makedirs(os.path.join(os.getcwd(), name, name, 'templates'))
    os.makedirs(os.path.join(os.getcwd(), name, name, 'static'))

    os.mkdir(os.path.join(os.getcwd(), name, '.venv'))
    os.makedirs(os.path.join(os.getcwd(), name, 'instance', 'uploads'))
    click.echo('Done!')

    click.echo('Creating first python scripts and configurations... ')
    

    templates_and_dest = {
       'init.pyt':  os.path.join(os.getcwd(), name, name, '__init__.py'),
       'views.pyt': os.path.join(os.getcwd(), name, name, 'views.py'),
       'index.htmlt': os.path.join(os.getcwd(), name, name, 'templates', 'index.html'),
       'configuration.pyt': os.path.join(os.getcwd(), name, name, 'ext', 'configuration.py'),
       'settings.tomlt': os.path.join(os.getcwd(), name, 'instance', 'settings.toml'),
       'manage.pyt': os.path.join(os.getcwd(), name, 'manage.py')
    }

    for template, destination in templates_and_dest.items():
        with open(destination, 'w') as f:
            template_file = get_template(template)
            f.write(template_file.render(name=name))

    click.echo('Done!')

    # Clonning project's own virtualenv
    click.echo(
        "ATTENTION: if this next stage fails, you should check if you do have venv on your system's Python.")
    click.echo('Clonning python onto its own virtual enviroment... ')
    subprocess.run(
        f'python3 -m venv {os.path.join(os.getcwd(), name, ".venv")}', shell=True)
    click.echo('Done!')

    # Requirements will help you do the basic startup of your virtualenv.
    add_support_to(name, 'flask')
    add_support_to(name, 'dynaconf')
    add_support_to(name, 'toml')
    add_support_to(name, 'flaskstarter')

    click.echo('If you do have other requirements, feel free to customize it.')

    click.echo('I will install the requirements for you.')
    install_requirements(name)
    click.echo('Done!')

    return 0


if __name__ == '__main__':
    flaskstarter(prog_name='flaskstarter')  # pylint: disable=unexpected-keyword-arg
