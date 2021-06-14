# flaskstarter
A Flask project start-up CLI to create modular ready projects.

Flaskstarter assumes you know about Flask microframework and its mechanics in a begginer level. It can be really helpfull if you are still using monolithic aproach, and needs to start using a modular architecture.

To install flaskstarter use the usual:

`pip install flaskstarter`

To see its help:

`flaskstarter --help`

To start a project:

`flaskstarter init project_name`

To see init's help:

`flaskstarter init --help`

After it you'll be prompted about some famous extensions to add to the project requirements.txt.

## What the project does for you

It creates project tree, a functional virtualenv on .venv, the init and routes files with a helloworld example and a shell/batch scripts to run the project with the virtual enviroment created. It now installs the requirements on project's .venv on POSIX systems.

## What the project does not do for you

It still can't update init file with modules configurations. On NT systems a batch file is created so user can run and install requirements.txt, but automation of this is still not well tested.

## Future

As a management tool it will be able to add new modules and inject its configurations onto projects. If you have a good idea, contact me.