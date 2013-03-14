Contributing
============

Getting the Source
------------------

Get the source for |appName| from this GitHub project: https://github.com/tctimmeh/htpc-launcher

:command:`git clone https://github.com/tctimmeh/htpc-launcher.git`

Setting Up a Development Environment
------------------------------------

Use a python virtualenv_ to work on |appName|. The included makefile will create an appropriate virtual environment
with all of the necessary third-party libraries installed. Run the following command to create the virtual environment:

:command:`make venv`

The virtual environment must then be activated before running tests, or building documentation or installation packages.
Activate the virtual environment with by running this command from the project root directory:

:command:`. venv/bin/activate`

For reference, the following third-party libraries are required to test and/or build |appName|:

  * pytest
  * mock
  * sphinx

Executing the Tests
-------------------

Run the |appName| tests by executing this command from the project root directory:

:command:`make test`

Continuous Integration
----------------------

This project is built and tested automatically by `Travis CI`_ after every commit to the main repository. Find the
latest build here: https://travis-ci.org/tctimmeh/htpc-launcher. See the Travis CI documentation for information about
how to configure the build: http://about.travis-ci.org/docs/.

Building Installation Package
-----------------------------

The |appName| source code includes a python :file:`setup.py` file to create a python installation package. The
Distribute_ python packaging library provides some additional functionality to the standard setup.py file. Here are
some common operations that can performed using the setup.py file.

Build a source distibution for testing
  :command:`./setup.py sdist`

Install the Development Working Copy to the Python Virtual Environment
  :command:`./setup.py develop`

Upload a New Version to the Python Package Index
  :command:`./setup.py sdist register upload`

  or

  :command:`make upload`

Building This Documentation
---------------------------

Build this documentation by running the following command from the project root directory:

:command:`make doc`

To build only the HTML or man page, run :command:`make html` or :command:`make man` respectively from the :file:`docs`
directory.

Making a New Release
--------------------

Follow these steps to release a new version:

1. Increment the product version number

  * Increment the release number if only bug fixes were made, the minor number if new features were added, or the major
    number if changes have broken backwards compatibility.

2. Tag the code with the new version number

3. Update the release notes by changing the 1.x label to the new version number. Create a new 1.x label.

4. Upload the new version to the Python Package Index by running :command:`make upload`

5. If any documentation was changed since the previous release, move the ``doc-latest`` branch to match the latest
   tagged release

.. _virtualenv: http://www.virtualenv.org/
.. _Distribute: http://packages.python.org/distribute/
.. _Travis CI: https://travis-ci.org/
