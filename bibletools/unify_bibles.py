#!/usr/bin/env python3

"""
Given two Bibles all in one file (with books and verses in any order), with one
verse per line, with lines like this:

BOOK_chapter_verse{TAB}Text of verse goes here...

... print out which verses are present in the first Bible but missing in the
second, and vice-versa.
"""

import sys

import util

def set_of_verses(fn):
    """Return the set of verses found in the given filename."""
    out = set()
    with open(fn) as infile:
        for line in infile:
            line = line.strip()
            verse, text = line.split("\t")
            if verse in out:
                util.dprint("WARNING duplicate verse {0} in {1}".format(
                    verse, fn))
            out.add(verse)
    return out

def main():
    left = set_of_verses(sys.argv[1])
    right = set_of_verses(sys.argv[2])
    print("[left but not right]")
    leftbutnotright = sorted(list(left - right))
    for verse in leftbutnotright:
        print(verse)
    print("[right but not left]")
    rightbutnotleft = sorted(list(right - left))
    for verse in rightbutnotleft:
        print(verse)

if __name__ == "__main__": main()
