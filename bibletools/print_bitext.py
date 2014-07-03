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
import os
import sys

import util
import tokenizer

## MA for es and gn
here = os.path.dirname(os.path.realpath(__file__))
paramorfo = os.path.realpath(
    os.path.join(here, "..", "dependencies", "ParaMorfo-1.1"))
sys.path.append(paramorfo)
import l3

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
    parser.add_argument('--tokenize', default=True, action='store_true')
    parser.add_argument('--notokenize', default=False, dest='tokenize', action='store_false')
    parser.add_argument('--lemmatize', default=False, action='store_true')
    return parser

def main():
    argparser = get_argparser()
    args = argparser.parse_args()
    sourcefn = args.source
    targetfn = args.target

    sourcebible = load_bible(sourcefn)
    targetbible = load_bible(targetfn)

    thetokenizer = tokenizer.gn_tokenizer()

    both = shared_verses(sourcebible, targetbible)
    for verseid in sorted(both):
        left, right = sourcebible[verseid], targetbible[verseid]
        if args.lowercase:
            left, right = left.lower(), right.lower()

        if args.tokenize:
            gnwords = thetokenizer.tokenize(right)
            right = " ".join(gnwords)
            eswords = thetokenizer.tokenize(left)
            left = " ".join(eswords)

        if args.lemmatize:
            gnlemmas = []
            gnwords = right.split()
            for gnword in gnwords:
                analyses = l3.anal('gn', gnword, raw=True)
                if analyses == []:
                    gnlemmas.append(gnword)
                else:
                    lemmas = "/".join(a[0] for a in analyses)
                    gnlemmas.append(lemmas)
            right = " ".join(gnlemmas)

            eslemmas = []
            eswords = left.split()
            for esword in eswords:
                analyses = l3.anal('es', esword, raw=True)
                if analyses == []:
                    eslemmas.append(esword)
                else:
                    lemmas = "/".join(a[0] for a in analyses)
                    # print("GOT A SPANISH ANALYSIS. word: {0} lemma: {1}".format(esword, lemmas))
                    eslemmas.append(lemmas)
            left = " ".join(eslemmas)
        print("{0} ||| {1}".format(left, right))
        break

if __name__ == "__main__": main()
