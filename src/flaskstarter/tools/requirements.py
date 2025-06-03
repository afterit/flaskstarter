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

import subprocess
import sys
from pathlib import Path

import click


def add_support_to(module: str, requirements_path: Path = None) -> bool:
    """
    Writes down the module name on project's requirements.txt.

    Args:
        module: Library name to add to requirements.txt
        requirements_path: Path to requirements.txt file. Defaults to current directory.

    Returns:
        bool: True if successful, False otherwise

    Raises:
        click.ClickException: If module name is invalid or file operations fail
    """
    # Validate module name (basic validation)
    if (
        not module
        or not module.replace("-", "").replace("_", "").replace(".", "").isalnum()
    ):
        raise click.ClickException(f"Invalid module name: {module}")

    if requirements_path is None:
        requirements_path = Path.cwd() / "requirements.txt"

    try:
        click.echo(f"Adding {module} support... ", nl=False)

        # Create file if it doesn't exist, append if it does
        with open(requirements_path, "a", encoding="utf-8") as requirements_file:
            requirements_file.write(f"{module}\n")

        click.echo("Done!")
        return True

    except (OSError, IOError) as e:
        raise click.ClickException(f"Couldn't write to requirements.txt: {e}")


def install_requirements(project_path: Path, requirements_path: Path = None) -> bool:
    """
    Installs requirements.txt in the project's virtual environment.

    Args:
        project_path: Path to the project directory
        requirements_path: Path to requirements.txt. Defaults to project_path/requirements.txt

    Returns:
        bool: True if installation successful, False otherwise

    Raises:
        click.ClickException: If installation fails or paths are invalid
    """
    if not isinstance(project_path, Path):
        project_path = Path(project_path)

    if not project_path.exists() or not project_path.is_dir():
        raise click.ClickException(f"Project directory does not exist: {project_path}")

    if requirements_path is None:
        requirements_path = project_path / "requirements.txt"

    if not requirements_path.exists():
        raise click.ClickException(f"Requirements file not found: {requirements_path}")

    # Detect virtual environment activation script
    venv_path = project_path / ".venv"
    if not venv_path.exists():
        raise click.ClickException(f"Virtual environment not found at: {venv_path}")

    # Determine the correct Python executable in the venv
    if sys.platform == "win32":
        python_executable = venv_path / "Scripts" / "python.exe"
    else:
        python_executable = venv_path / "bin" / "python"

    if not python_executable.exists():
        raise click.ClickException(
            f"Python executable not found in venv: {python_executable}"
        )

    try:
        click.echo(f"Installing requirements from {requirements_path}...")

        # Use the venv's Python directly instead of shell activation
        cmd = [
            str(python_executable),
            "-m",
            "pip",
            "install",
            "-r",
            str(requirements_path),
        ]

        result = subprocess.run(cmd, capture_output=True, text=True, check=True)

        click.echo("Requirements installed successfully!")
        return True

    except subprocess.CalledProcessError as e:
        error_msg = f"Failed to install requirements: {e.stderr if e.stderr else e}"
        raise click.ClickException(error_msg)
    except FileNotFoundError:
        raise click.ClickException("pip command not found in virtual environment")


def create_virtual_environment(project_path: Path, python_version: str = None) -> bool:
    """
    Creates a virtual environment for the project.

    Args:
        project_path: Path where to create the virtual environment
        python_version: Specific Python version to use (optional)

    Returns:
        bool: True if creation successful, False otherwise

    Raises:
        click.ClickException: If virtual environment creation fails
    """
    if not isinstance(project_path, Path):
        project_path = Path(project_path)

    venv_path = project_path / ".venv"

    if venv_path.exists():
        click.echo("Virtual environment already exists.")
        return True

    try:
        click.echo(f"Creating virtual environment at {venv_path}...")

        # Build command
        if python_version:
            # Try to use specific Python version
            cmd = [f"python{python_version}", "-m", "venv", str(venv_path)]
        else:
            # Use current Python interpreter
            cmd = [sys.executable, "-m", "venv", str(venv_path)]

        result = subprocess.run(cmd, capture_output=True, text=True, check=True)

        click.echo("Virtual environment created successfully!")
        return True

    except subprocess.CalledProcessError as e:
        error_msg = (
            f"Failed to create virtual environment: {e.stderr if e.stderr else e}"
        )
        raise click.ClickException(error_msg)
    except FileNotFoundError:
        raise click.ClickException("Python interpreter not found")


def upgrade_pip_in_venv(project_path: Path) -> bool:
    """
    Upgrades pip in the project's virtual environment.

    Args:
        project_path: Path to the project directory

    Returns:
        bool: True if upgrade successful, False otherwise

    Raises:
        click.ClickException: If pip upgrade fails
    """
    if not isinstance(project_path, Path):
        project_path = Path(project_path)

    venv_path = project_path / ".venv"

    # Determine the correct Python executable in the venv
    if sys.platform == "win32":
        python_executable = venv_path / "Scripts" / "python.exe"
    else:
        python_executable = venv_path / "bin" / "python"

    if not python_executable.exists():
        raise click.ClickException(
            f"Python executable not found in venv: {python_executable}"
        )

    try:
        click.echo("Upgrading pip in virtual environment...")

        cmd = [str(python_executable), "-m", "pip", "install", "--upgrade", "pip"]

        result = subprocess.run(cmd, capture_output=True, text=True, check=True)

        click.echo("Pip upgraded successfully!")
        return True

    except subprocess.CalledProcessError as e:
        error_msg = f"Failed to upgrade pip: {e.stderr if e.stderr else e}"
        raise click.ClickException(error_msg)
