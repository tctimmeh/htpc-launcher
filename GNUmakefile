VENV_DIR = venv

.PHONY: test

test: venv
	. $(VENV_DIR)/bin/activate && py.test test
	
venv:
	virtualenv venv
	. $(VENV_DIR)/bin/activate && pip install pytest mock

