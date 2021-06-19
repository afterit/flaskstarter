VERSION ?= 0.2.1
TEMP_PROJECT ?= temp

# Deploy recipes
build:
	python setup.py sdist
	python setup.py bdist_wheel --universal

deploy: build
	twine upload dist/flaskstarter-$(VERSION)*

# Development recipes
.venv/bin/activate: requirements-dev.txt
    python3 -m venv .venv
    ./.venv/bin/pip install -r requirements-dev.txt

install: .venv/bin/activate
	pip install -e . --upgrade

run: install
	flaskstarter init $(TEMP_PROJECT)
	cd $(TEMP_PROJECT); python manage.py runserver

uninstall:
	pip uninstall -y flaskstarter

clean: devuninstall
	rm -rf $(TEMP_PROJECT)
	rm -rf build
	rm -rf dist
	find . | grep -E "(__pycache__|\.pyc|\.pyo$)" | xargs rm -rf
	find . | grep -E "(egg-info$)" | xargs rm -rf

.PHONY: install run uninstall clean build deploy
