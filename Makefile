VERSION ?= 0.2.1
TEMP_PROJECT ?= temp
VENV := .venv

check:
	cat -e -t -v Makefile

all: venv

build: venv
	./$(VENV)/bin/python setup.py sdist
	./$(VENV)/bin/python setup.py bdist_wheel --universal

deploy: build
	twine upload dist/flaskstarter-$(VERSION)*

$(VENV)/bin/activate: requirements-dev.txt
	python3 -m venv $(VENV)
	./$(VENV)/bin/pip install -r requirements-dev.txt

venv: $(VENV)/bin/activate

install: venv
	./$(VENV)/bin/pip install -e . --upgrade

run: install
	flaskstarter init $(TEMP_PROJECT)
	cd $(TEMP_PROJECT); ./$(VENV)/bin/python manage.py runserver

uninstall:
	./$(VENV)/bin/pip uninstall -y flaskstarter

clean:
	rm -rf $(TEMP_PROJECT)
	rm -rf build
	rm -rf dist
	rm -rf $(VENV)
	find . | grep -E "(__pycache__)" | xargs rm -rf
	find . | grep -E "(egg-info)" | xargs rm -rf

.PHONY: install run uninstall clean build deploy
