HTPC Launcher
=============

HTPC Launcher is a program for launching full-screen applications. It is designed for use in an environment where only
one of several resource-intensive applications should be run at once. HTPC Launcher responds to
LIRC [#lirc]_ key presses by starting a configured application and stopping any others that may
still be running.

For example, if HTPC Launcher is configured for `XBMC <http://xbmc.org/>`_ and `Steam <http://steampowered.com/>`_,
then pressing the configured LIRC key for XBMC will launch that program. Next, if the button for Steam is pressed,
HTPC Launcher will shut down XBMC and launch Steam.

This document describes how to install, configure, and use HTPC Launcher.

Contents:

.. toctree::
   :maxdepth: 2

   configure
   contrib

Installation
------------

Install HTPC Launcher using :program:`pip`:

:command:`pip install htpc-launcher`

Usage
-----

Configure HTPC Launcher by creating a configuration file as described in :doc:`configure`. HTPC Launcher will not run
without a configuration file.

Run HTPC Launcher by executing:

:command:`htpc-launch`

HTPC Launcher will respond to LIRC codes by starting and stopping your configured applications.

Inspect the run-time log file to diagnose any problems. The log file is located in :file:`~/.ir-switch.log`.

.. rubric:: Footnotes

.. [#lirc] Linux Infrared Remote Control (http://lirc.org/) is used to read IR signals from your remote control.
