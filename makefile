VERSION=0.1.4

all: build upload

build:
	python setup.py sdist
	python setup.py bdist wheel --universal

upload:
	twine upload dist/flaskstarter-$(VERSION)*
