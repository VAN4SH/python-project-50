install:
	poetry install

uninstall:
	pip uninstall hexlet-code -y

publish:
	poetry publish --dry-run

gendiff:
	poetry run gendiff

build:
	python3 setup.py sdist bdist_wheel

package-install:
	pip install .

test:
	poetry run pytest

lint:
	poetry run flake8 gendiff tests


