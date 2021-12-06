publish: build
	poetry publish

build:
	poetry build

format:
	black -l 80 .

clear:
	rm -rf .pytest_cache
	rm -rf dist
	rm -rf */__pycache__
