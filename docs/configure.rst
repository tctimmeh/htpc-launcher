Configuration
=============

|appName| requires configuration before use. It looks for a configuration file called |confFile| in
the user's home directory.

The configuration file must be formatted according to the rules for the python `Config Parser`_ module. It consists of
sections denoted by headers in square brackets (``[]``) which contain a series of name/value pairs for each
configuration item.

For example::

  [startup]
  launch = KEY_YELLOW

  [KEY_YELLOW]
  process = xbmc
  search = xbmc.bin

  [KEY_BLUE]
  process = steam
  search = .local/share/Steam/.+/steam
  needsKill = true


There are two types of sections:

* **startup** -- contains global configuration for |appName|
* **key** -- contains options for an application bound to an LIRC key code

Global Configuration
--------------------

The following options are recognized in the ``startup`` section.

launch
  The name of an LIRC key code to activate when |appName| starts. This must match one of the configured key
  sections.

Key Configuration
-----------------

Key sections describe an application that |appName| will be responsible for running. The section name must match
an LIRC key code (see `Find LIRC Key Codes`_ for help finding the key codes for your remote). Within each section the following
configuration items are recognized.

process
  The process to run when this LIRC key is received.

search
  When |appName| needs to stop an application it searches for the appropriate process using this perl-compatible
  regular expression.

needsKill
  Set this option to true if the application does not shutdown correctly in response to a SIGTERM signal. This will
  cause |appName| to stop the application by sending it SIGKILL instead.

Tips For Creating the Configuration
-----------------------------------

Find LIRC Key Codes
###################

Run the :command:`irw` command to see the key names as interpretted by LIRC.

For example, this is output of ``irw`` after pressing the "1" key on a typical remote control::

  $ irw
  000000037ff07bfe 00 KEY_1 mceusb
  000000037ff07bfe 01 KEY_1 mceusb


.. _Config Parser: http://docs.python.org/2/library/configparser.html
