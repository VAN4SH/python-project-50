build:
	python3 setup.py sdist bdist_wheel

package-install:
	pip install .