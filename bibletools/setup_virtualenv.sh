#!/bin/bash

virtualenv -p /usr/bin/python3 venv
. venv/bin/activate
pip install beautifulsoup4
pip install numpy
pip install https://github.com/nltk/nltk/tarball/develop

