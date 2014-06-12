"""Utilities for standardizing names of Bible books."""

import os
from collections import defaultdict

LOOKUP = None

KNOWNBOOKS = set()

def load_table():
    global LOOKUP
    here = os.path.dirname(os.path.realpath(__file__))
    fn = here + os.path.sep + "booknames.txt"
    LOOKUP = defaultdict(str)
    with open(fn) as infile:
        for line in infile:
            bookcode, name = line.strip().split(maxsplit=1)
            LOOKUP[name] = bookcode
            KNOWNBOOKS.add(bookcode)

if not LOOKUP:
    load_table()

def code(name):
    return LOOKUP[name]

def knownbooks():
    return KNOWNBOOKS
