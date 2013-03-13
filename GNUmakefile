VENV_DIR = venv

DEPENDENCIES = pytest mock sphinx

.PHONY: test clean doc

all: test doc

test: venv
	. $(VENV_DIR)/bin/activate && py.test test

clean:
	@find . -name \*.pyc | xargs rm -f
	@rm -f distribute-*
	@rm -rf build dist *.egg-info
	
upload: clean
	./setup.py sdist register upload

venv:
	virtualenv venv
	. $(VENV_DIR)/bin/activate && pip install $(DEPENDENCIES)

doc: venv
	. $(VENV_DIR)/bin/activate && cd docs && $(MAKE) html man

dependencies:
	pip install $(DEPENDENCIES)
