# flaskstarter
A Flask project start-up CLI to create a modular ready projects.

To install flaskstarter use the usual:

`pip install flaskstarter`

To see its help:

`flaskstarter --help`

To start a project:

`flaskstarter -n project_name`

After it you'll be prompted about some famous extensions to add to the project requirements.txt.

## What the project does for you

It creates project tree, a functional virtualenv on .venv, the init and routes files with a helloworld example and a shell/batch scripts to run the project with the virtual enviroment created.

## What the project does not do for you

As you may want to add some more requirements, flaskstarter wont install the requirements, so you need to run `pip install -r requirements.txt` before any use of the project created.