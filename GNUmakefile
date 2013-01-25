VENV_DIR = venv

.PHONY: test clean

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
	. $(VENV_DIR)/bin/activate && pip install pytest mock sphinx

