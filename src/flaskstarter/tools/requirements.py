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


def add_support_to(name, module):
    """Writes down the module name on project's requirements.txt.

    Warning: called only on project's creation time.

    Args:
        name (string): Project's name.
        module (string): Library to add to requirements.txt.
    """
    try:
        requirements = open(os.path.join(
            os.getcwd(), name, 'requirements.txt'), 'a')
        click.echo(f'Adding {module} support... ')
        requirements.write(f'{module}{os.linesep}')
        click.echo('Done!')
    except:
        click.echo(f"Couldn't create requirements.txt on {name}")
    finally:
        requirements.close()


def install_requirements(name):
    """Installs the requirements.txt on destination project's virtual environment.

    Warning: MS Windows wasn't tested yet.

    Args:
        name (string): Project's name.
    """
    cmd = ''
    if os.name == 'posix':
        cmd = f'. {os.path.join(os.getcwd(), name, ".venv", "bin", "activate")}; pip install -r {os.path.join(os.getcwd(), name, "requirements.txt")};'
    elif os.name == 'nt':
        cmd = f'call {os.path.join(os.getcwd(), name, ".venv", "Scripts", "activate")}; pip install -r {os.path.join(os.getcwd(), name, "requirements.txt")};'
    subprocess.call(cmd, shell=True)
