VERSION=0.2
TEMPPROJECT=temp

all: build upload

build:
	python setup.py sdist
	python setup.py bdist_wheel --universal

upload:
	twine upload dist/flaskstarter-$(VERSION)*

devrun:
	pip install -e . --upgrade
	flaskstarter init $(TEMPPROJECT)
	cd $(TEMPPROJECT); python manage.py runserver

devclean: devuninstall
	rm -rf $(TEMPPROJECT)
	rm -rf build/*

devuninstall:
	pip uninstall -y flaskstarter