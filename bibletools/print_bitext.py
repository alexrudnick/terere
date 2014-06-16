#!/usr/bin/env python3

"""
Given two Bibles all in one file (with books and verses in any order), with one
verse per line, with lines like this:

BOOK_chapter_verse{TAB}Text of verse goes here...

... for all the verses that are present in both, print those two verses joined
by a |||, source on the left and target on the right, ready for alignment.

Also optionally do lowercasing, tokenization and lemmatization.
"""

import argparse

import util

def load_bible(fn):
    out = {}
    with open(fn) as infile:
        for line in infile:
            line = line.strip()
            verseid, text = line.split('\t')
            ## just to check...
            if verseid in out:
                util.dprint("{0} already in table {1}".format(verseid,
                    "DIFFERENT" if text != out[verseid] else "SAME"))
            out[verseid] = text
    return out

def shared_verses(bible1, bible2):
    """Given two hash tables, return the set of keys present in both."""
    keys1 = set(bible1.keys())
    keys2 = set(bible2.keys())
    both = keys1.intersection(keys2)
    util.dprint("intersection has %0.2f%% from keys1, %0.2f%% from keys2" %
        (len(both) / len(keys1) * 100, len(both) / len(keys2) * 100))
    return both

def get_argparser():
    """Build the argument parser for main."""
    parser = argparse.ArgumentParser(description='print_bitext')
    parser.add_argument('--source', type=str, required=True)
    parser.add_argument('--target', type=str, required=True)
    parser.add_argument('--lowercase', default=False, action='store_true')
    return parser

def main():
    argparser = get_argparser()
    args = argparser.parse_args()
    sourcefn = args.source
    targetfn = args.target
    lowercase = args.lowercase

    sourcebible = load_bible(sourcefn)
    targetbible = load_bible(targetfn)

    both = shared_verses(sourcebible, targetbible)
    for verseid in sorted(both):
        left, right = sourcebible[verseid], targetbible[verseid]
        if lowercase:
            left, right = left.lower(), right.lower()
        print("{0} ||| {1}".format(left, right))

if __name__ == "__main__": main()
