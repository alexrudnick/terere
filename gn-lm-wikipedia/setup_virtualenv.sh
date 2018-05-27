#!/bin/bash

virtualenv -p /usr/bin/python3 venv
. venv/bin/activate
pip install https://github.com/nltk/nltk/archive/3.0.4.zip
