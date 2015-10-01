#!/usr/bin/env python3

"""
Given two Bibles all in one file (with books and verses in any order), with one
verse per line, with lines like this:

BOOK_chapter_verse{TAB}Text of verse goes here...

... for all the verses that are present in both, print those two verses joined
by a |||, source on the left and target on the right, ready for alignment.

Also optionally do lowercasing and tokenization.
"""

import argparse
import os
import sys

import util
import tokenizer

LANGUAGES = "en es gn qu".split()

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

def shared_verseids(bible1, bible2):
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
    parser.add_argument('--source_tokenize', default=False, action='store_true')
    parser.add_argument('--target_tokenize', default=False, action='store_true')
    parser.add_argument('--out', type=str, required=False)
    return parser

def collect_shared_verses(sourcebible, targetbible, verseids,
    source_tokenize=False, target_tokenize=False,
    lowercase=False, sl=None, tl=None):
    """Returns one list of strings: just the surface one. If
    lemmatize is False, return None for that first output."""

    assert sl in LANGUAGES, "need to specify source language"
    assert tl in LANGUAGES, "need to specify target language"

    thetokenizer = tokenizer.gn_tokenizer()
    lemmatized_out = []
    surface_out = []
    for verseid in sorted(verseids):
        left, right = sourcebible[verseid], targetbible[verseid]
        if lowercase:
            left, right = left.lower(), right.lower()

        if source_tokenize:
            sourcewords = thetokenizer.tokenize(left)
            left = " ".join(sourcewords)
        if target_tokenize:
            targetwords = thetokenizer.tokenize(right)
            right = " ".join(targetwords)

        verseline = "{0} ||| {1}".format(left, right)
        surface_out.append(verseline)
    return surface_out

def main():
    argparser = get_argparser()
    args = argparser.parse_args()
    sourcefn = args.source
    targetfn = args.target

    sourcelanguage = sourcefn.split(".")[1]
    targetlanguage = targetfn.split(".")[1]

    sourcebible = load_bible(sourcefn)
    targetbible = load_bible(targetfn)

    verseids = shared_verseids(sourcebible, targetbible)

    surface = collect_shared_verses(sourcebible, targetbible, verseids,
                                    source_tokenize=args.source_tokenize,
                                    target_tokenize=args.target_tokenize,
                                    lowercase=args.lowercase,
                                    sl=sourcelanguage,
                                    tl=targetlanguage)

    try:
        outfile = sys.stdout
        if args.out:
            outfile = open(args.out, "w")
        for line in surface:
            print(line, file=outfile)
    finally:
        if args.out:
            outfile.close()

if __name__ == "__main__": main()
