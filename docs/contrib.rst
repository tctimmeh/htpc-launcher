Contributing
============

Getting the Source
------------------

Get the source for HTPC Launcher from this GitHub project: https://github.com/tctimmeh/htpc-launcher

:command:`git clone https://github.com/tctimmeh/htpc-launcher.git`

Setting Up a Development Environment
------------------------------------

Use a python virtualenv_ to work on HTPC Launcher. The included makefile will create an appropriate virtual environment
with all of the necessary third-party libraries installed. Run the following command to create the virtual environment:

:command:`make venv`

The virtual environment must then be activated before running tests, or building documentation or installation packages.
Activate the virtual environment with by running this command from the project root directory:

:command:`. venv/bin/activate`

.. note::

   For reference, the following third-party libraries are required to test and/or build HTPC Launcher:

   * pytest
   * mock
   * sphinx

Executing the Tests
-------------------

Run the HTPC Launcher tests by executing this command from the project root directory:

:command:`make test`

Building Installation Package
-----------------------------

The HTPC Launcher source code includes a python :file:`setup.py` file to create a python installation package. The
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

or this command from the :file:`docs` directory:

:command:`make html`

.. _virtualenv: http://www.virtualenv.org/
.. _Distribute: http://packages.python.org/distribute/
