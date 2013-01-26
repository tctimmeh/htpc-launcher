|appName|
=============

|appName| is a program for launching full-screen applications. It is designed for use in an environment where only
one of several resource-intensive applications should be run at once. |appName| responds to
LIRC [#lirc]_ key presses by starting a configured application and stopping any others that may
still be running.

For example, if |appName| is configured for `XBMC <http://xbmc.org/>`_ and `Steam <http://steampowered.com/>`_,
then pressing the configured LIRC key for XBMC will launch that program. Next, if the button for Steam is pressed,
|appName| will shut down XBMC and launch Steam.

.. toctree::
   :maxdepth: 2

   configure
   contrib

Installation
------------

Install |appName| using :program:`pip`:

  $ pip install |projName|

Usage
-----

Configure |appName| by creating a configuration file as described in :doc:`configure`. |appName| will not run
without a configuration file.

Run |appName| by executing:

  $ |runCmd|

|appName| will respond to LIRC codes by starting and stopping your configured applications.

Inspect the run-time log file to diagnose any problems. The log file is located in |logFile|.

.. rubric:: Footnotes

.. [#lirc] Linux Infrared Remote Control (http://lirc.org/) is used to read IR signals from your remote control.
