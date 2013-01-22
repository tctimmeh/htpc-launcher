#!/usr/bin/env python

from distribute_setup import use_setuptools
use_setuptools()

from setuptools import setup, find_packages

setup(
  name = "htpc-launcher",
  version = "1.0",
  packages = find_packages(),

  author = "Tim Court",
  author_email = "tctimmeh@gmail.com",
  description = "Launch, and switch between, full-screen applications",
  url = "https://github.com/tctimmeh/htpc-launcher",

  classifiers = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: End Users/Desktop',
    'Topic :: Multimedia',
    'License :: Public Domain',
    'Operating System :: POSIX :: Linux',
  ],

  entry_points = {
    'console_scripts': [
      'htpc-launch = irswitch.app:main',
    ],
  }
)
