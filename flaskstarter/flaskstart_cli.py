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

import os
import click

from flaskstarter import __version__

from flaskstarter.tools.templating import get_template


@click.group()
@click.version_option(version=f"{__version__}")
def flaskstarter():
    """A program to start a Flask project under a modular structure."""


@flaskstarter.command()
@click.argument(
    "name",
)
def init(name: str):
    """Creates the project's source tree.

    Args:

      - name (str): Project's main package's name to create. If it's a dot, will use current directory as project's name.

    """
    # All directories and basic python files are created here
    click.echo("Creating project's source tree... ", nl=False)

    if name == ".":
        name = os.path.split(os.getcwd())[1]

    try:
        os.mkdir(os.path.join(os.getcwd(), name))
    except FileExistsError:
        click.echo(
            f'Project or module with name "{name}" already exists. Exiting.'
        )
        exit(0)

    os.makedirs(os.path.join(os.getcwd(), name, "ext"))
    ext_is_package = open(
        os.path.join(os.getcwd(), name, "ext", "__init__.py"), "w"
    )
    ext_is_package.close()
    os.makedirs(os.path.join(os.getcwd(), name, "blueprints"))
    blueprint_is_package = open(
        os.path.join(os.getcwd(), name, "ext", "__init__.py"), "w"
    )
    blueprint_is_package.close()
    app_is_package = open(os.path.join(os.getcwd(), name, "__init__.py"), "w")
    app_is_package.close()

    os.makedirs(os.path.join(os.getcwd(), name, "templates"))
    os.makedirs(os.path.join(os.getcwd(), name, "static"))

    os.makedirs(os.path.join(os.getcwd(), "instance", "uploads"))
    click.echo("Done!")

    click.echo("Creating first python scripts and configurations... ", nl=False)

    templates_and_dest = {
        "app.pyt": os.path.join(os.getcwd(), name, "app.py"),
        "views.pyt": os.path.join(os.getcwd(), name, "views.py"),
        "index.htmlt": os.path.join(
            os.getcwd(), name, "templates", "index.html"
        ),
        "configuration.pyt": os.path.join(
            os.getcwd(), name, "ext", "configuration.py"
        ),
        "settings.tomlt": os.path.join(
            os.getcwd(), "instance", "settings.toml"
        ),
        "manage.pyt": os.path.join(os.getcwd(), "manage.py"),
    }

    for template, destination in templates_and_dest.items():
        with open(destination, "w") as f:
            template_file = get_template(template)
            f.write(template_file.render(name=name))

    click.echo("Done!")

    # Requirements will help you do the basic startup of your virtualenv.
    baserequirements = [
        "Flask",
        "dynaconf",
        "toml",
        f"flaskstarter=={__version__}",
    ]
    for requirement in baserequirements:
        click.echo(f'Please, add "{requirement}" to the list of dependencies.')

    click.echo("Project created!")

    return 0


if __name__ == "__main__":
    flaskstarter(
        prog_name="flaskstarter"
    )  # pylint: disable=unexpected-keyword-arg
