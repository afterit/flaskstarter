# flaskstarter 0.5.3

![](https://img.shields.io/pypi/l/flaskstarter) ![](https://img.shields.io/pypi/v/flaskstarter) ![](https://img.shields.io/pypi/wheel/flaskstarter) 

A Flask project start-up CLI to create modular ready projects.

Flaskstarter assumes you know about Flask microframework and its mechanics in a begginer level. It can be really helpful if you are still using monolithic aproach, and needs to start using a modular architecture.

It also assumes you are using Python 3.6+.

> Flaskstarter recommends the use of a python virtual environment for project
> to work safely and isolated from your systems binnaries. Activate it before
> the next steps.

To install flaskstarter use the usual:

`pip install flaskstarter`

To see its version:

`flaskstarter --version`

To see its help:

`flaskstarter --help`

To start a project, create its folder and:

`flaskstarter init main_module_name`

If you do want to use the same project's root folder as main module name:

`flaskstarter init .`

> It won't create a requirements.txt on its own anymore, so you feel free to choose your tools.

To see init's help:

`flaskstarter init --help`

Now, after project creation, you can  make full use of manage.py, a script
with a CLI that may help you to automate some tasks inside project tree.

By now you can create a blueprint structure by typing the bellow on project root:

`$ python manage.py plug-blueprint [blueprint_name]`

If it will work as an API blueprint, that's enough. But maybe it is not and you want to use private templates related only to this blueprint. This is solved by adding a '-t' or '--templates' to the above command.

After that, flaskstarter goes onto instance/settings.toml file to register the blueprint on it. There is an EXTENSIONS variable where you can list all the plugins to autoimport if you create any by hand. It uses factory design.

Most of the times you are adding some extensions and middlewares to your app, so
you can add an empty skelleton to instanciate and plug to app by typing:

`$ python manage.py plug-extension [name]`

As with blueprints, flaskstarter registers extensions on instance/settings.

To run your app you can use the bellow on project root:

`$ python manage.py runserver`

Ask manage.py for runserver help to see its options.

Now it is possible to plug a database and a migration extensions to the project. For a first experience Flaskstarter is running with flask-sqlalchemy and flask-migrate. The templates that generate the kickoff database use sqlite and the simplest thing possible. You will be able to plug a database by running:

`$ python manage.py plug-database`

When plug-database is ran, the manage script will create the migrations folder as 
Alembic requires. Once it is created the following commands will be available.

This will generate a migration script with Example as message:

`$ python manage.py db-migrate Example`

This upgrades the database:

`$ python manage.py db-upgrade`

If anything undesirable happens, this will downgrade the database:

`$ python manage.py db-downgrade`

For other Flask-Migrate commands, you can export FLASK_APP on your shell and use
flask db (command) as its documentation guides.

## What the project does for you

It creates project tree, a functional virtualenv on .venv, the init and routes files with a helloworld example and a manage.py script to run the project with the virtual enviroment created and attach blueprints to it. It now installs the requirements on project's .venv on POSIX systems. Feel free to change to poetry and pyproject.toml pattern.

A word of warning: when commiting and pushing your project to versioning servers, remember to put instance folder into .gitignore, if not yet. And then remember to place it into deploy destination.

## What the project does not do for you

It doesn't force you to use poetry or any other tool but flask, toml and dynaconf on the Flask project created.

## Future

- Add automated tests for development enviroment of flaskstarter
- Work on a better architecture for the generated project
- Start new extensions by manage.py creating an empty skeleton

## How can you help on flaskstarter development?

Feel free to clone it and send us pull requests! Remember to comment the decisions you make so they can be better reviewed.
