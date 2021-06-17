# flaskstarter
A Flask project start-up CLI to create modular ready projects.

Flaskstarter assumes you know about Flask microframework and its mechanics in a begginer level. It can be really helpfull if you are still using monolithic aproach, and needs to start using a modular architecture.

It also assumes you are using Python 3.6+.

To install flaskstarter use the usual:

`pip install flaskstarter`

To see its help:

`flaskstarter --help`

To start a project:

`flaskstarter init project_name`

To see init's help:

`flaskstarter init --help`

Now, after project creation, you can enter on its directory and make full use of manage.py, a script with a CLI that may help you to automate some tasks inside project tree.

By now you can create a blueprint structure by typing the bellow on project root:

`$ python manage.py createblueprint [blueprint_name]`

After that, remember to go on the app init file to register the blueprint on it.

To run your app you can use the bellow on project root:

`$ python manage.py runserver`

## What the project does for you

It creates project tree, a functional virtualenv on .venv, the init and routes files with a helloworld example and a manage.py script to run the project with the virtual enviroment created and attach blueprints to it. It now installs the requirements on project's .venv on POSIX systems.

## What the project does not do for you

It still can't update init file with modules configurations. By now blueprints aren't created with custom folder.

## Future

Add more power to manage.py.