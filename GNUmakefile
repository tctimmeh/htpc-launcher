VENV_DIR = venv
DESTDIR ?= /

PROJECT = $(shell python -c "from htpclauncher import PROJECT_NAME; print PROJECT_NAME")
VERSION = $(shell python -c "from htpclauncher import VERSION; print VERSION")

DPKG_BUILD_DIR = $(PROJECT)-$(VERSION)

.PHONY: test clean doc install dpkg

all: clean test doc

test: venv
	. $(VENV_DIR)/bin/activate && py.test test

clean:
	@find . -name \*.pyc | xargs rm -f
	@find . -name __pycache__ | xargs rm -rf
	@rm -f distribute-*
	@rm -rf build dist *.egg-info
	@rm -rf $(PROJECT)-* $(PROJECT)_*.tar.gz *.dsc *.deb *.changes
	cd docs && make clean
	
upload: clean
	./setup.py sdist register upload

venv:
	virtualenv venv
	. $(VENV_DIR)/bin/activate && pip install pytest mock sphinx

doc: venv
	. $(VENV_DIR)/bin/activate && cd docs && $(MAKE) html man

install: doc
	echo DEST DIR is $(DESTDIR)
	./setup.py install --root $(DESTDIR) --no-compile --install-scripts /usr/bin

dpkg: clean
	mkdir -p $(DPKG_BUILD_DIR)
	-cp -R * $(DPKG_BUILD_DIR)
	-rm -rf $(DPKG_BUILD_DIR)/venv
	cd $(DPKG_BUILD_DIR) && dpkg-buildpackage -us -uc
