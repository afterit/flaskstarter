VERSION=0.1.6
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

devclean:
	rm -rf $(TEMPPROJECT)

devuninstall:
	pip uninstall -y flaskstarter