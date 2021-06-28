# flaskstarter
A Flask project start-up CLI to create modular ready projects.

Flaskstarter assumes you know about Flask microframework and its mechanics in a begginer level. It can be really helpfull if you are still using monolithic aproach, and needs to start using a modular architecture.

It also assumes you are using Python 3.6+.

To install flaskstarter use the usual:

`pip install flaskstarter --require-hashes`

To see its help:

`flaskstarter --help`

To start a project:

`flaskstarter init project_name`

To see init's help:

`flaskstarter init --help`

Now, after project creation, you can enter on its directory and make full use of manage.py, a script with a CLI that may help you to automate some tasks inside project tree.

By now you can create a blueprint structure by typing the bellow on project root:

`$ python manage.py plug-blueprint [blueprint_name]`

If it will work as an API blueprint, that's enough. But maybe it is not and you want to use private templates related only to this blueprint. This is solved by adding a '-t' or '--templates' to the above command.

After that, remember to go onto app init file to register the blueprint on it. There is an EXTENSIONS variable where you can list all the plugins to autoimport. It uses factory design.

To run your app you can use the bellow on project root:

`$ python manage.py runserver`

Ask manage.py for runserver help to see its options.

Now it is possible to plug a database and a migration extensions to the project. For a first experience Flaskstarter is running with flask-sqlalchemy and flask-migrate. The templates that generate the kickoff database use sqlite and the simplest thing possible. You will be able to plug a database by running:

`$ python manage.py plug-database`

For migrations, you'll have Flask-migrate interface for now, but remember to have your models connected to your app, maybe doing a simple import on the views file, or entities won't be added to database.

## What the project does for you

It creates project tree, a functional virtualenv on .venv, the init and routes files with a helloworld example and a manage.py script to run the project with the virtual enviroment created and attach blueprints to it. It now installs the requirements on project's .venv on POSIX systems. Feel free to change to poetry and pyproject.toml pattern.

A word of warning: when commiting and pushing your project to versioning servers, remember to put instance folder into .gitignore, if not yet. And then remember to place it into deploy destination.

## What the project does not do for you

It doesn't force you to use pip, poetry or any other tool but flask, toml and dynaconf on the Flask project created.

## Future

Add more power to manage.py; maybe database configuration and migrations. (it is running but not fully tested)