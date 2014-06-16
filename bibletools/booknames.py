"""Utilities for standardizing names of Bible books."""

import os
import sys
from collections import defaultdict

LOOKUP = None
NUMBER_LOOKUP = None

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

def load_number_table():
    global NUMBER_LOOKUP
    here = os.path.dirname(os.path.realpath(__file__))
    fn = here + os.path.sep + "booknumbers.txt"
    NUMBER_LOOKUP = defaultdict(str)
    with open(fn) as infile:
        for line in infile:
            booknum, bookcode = line.strip().split(maxsplit=1)
            NUMBER_LOOKUP[booknum] = bookcode

if not LOOKUP:
    load_table()

if not NUMBER_LOOKUP:
    load_number_table()

def code(name):
    return LOOKUP[name]

def knownbooks():
    return KNOWNBOOKS

def booknum_to_code(booknum):
    return NUMBER_LOOKUP[booknum]
