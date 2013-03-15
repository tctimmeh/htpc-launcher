VENV_DIR = venv

DEV_DEPS = pytest mock sphinx coverage pytest-cov coveralls

.PHONY: all test clean doc upload dependencies

all: test doc

test: venv
	. $(VENV_DIR)/bin/activate && py.test --cov htpclauncher test

clean:
	@find . -name \*.pyc | xargs rm -f
	@rm -f distribute-*
	@rm -rf build dist *.egg-info
	
upload: clean
	./setup.py sdist register upload

venv:
	virtualenv venv
	. $(VENV_DIR)/bin/activate && pip install $(DEV_DEPS)

doc: venv
	. $(VENV_DIR)/bin/activate && cd docs && $(MAKE) html man

dependencies:
	pip install $(DEV_DEPS)
