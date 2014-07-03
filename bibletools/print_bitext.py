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
    parser.add_argument('--tokenize', default=True, action='store_true')
    parser.add_argument('--notokenize', default=False, dest='tokenize', action='store_false')
    parser.add_argument('--lemmatize', default=False, action='store_true')
    parser.add_argument('--out', type=str, required=True)
    return parser

def analyze(lang, word):
    """Return either a morphological analysis of the word, or if we can't do
    that, just the surface form again."""
    analyses = l3.anal(lang, word, raw=True)
    if analyses == []:
        return word
    lemmas = set(a[0] for a in analyses)
    return "/".join(lemma for lemma in lemmas)

def collect_shared_verses(sourcebible, targetbible, verseids,
    tokenize=False, lowercase=False, lemmatize=False):
    """Returns two lists of strings, the lemmatized one and the surface one. If
    lemmatize is False, return None for that first output."""
    thetokenizer = tokenizer.gn_tokenizer()
    lemmatized_out = []
    surface_out = []
    for verseid in sorted(verseids):
        left, right = sourcebible[verseid], targetbible[verseid]
        if lowercase:
            left, right = left.lower(), right.lower()

        if tokenize:
            gnwords = thetokenizer.tokenize(right)
            right = " ".join(gnwords)
            eswords = thetokenizer.tokenize(left)
            left = " ".join(eswords)

        verseline = "{0} ||| {1}".format(left, right)
        surface_out.append(verseline)

        if lemmatize:
            gnwords = right.split()
            gnlemmas = [analyze("gn", word) for word in gnwords]
            right = " ".join(gnlemmas)
            eswords = left.split()
            eslemmas = [analyze("es", word) for word in eswords]
            left = " ".join(eslemmas)
        verseline = "{0} ||| {1}".format(left, right)
        lemmatized_out.append(verseline)

    if not lemmatize:
        lemmatized_out = None
    return lemmatized_out, surface_out

def main():
    argparser = get_argparser()
    args = argparser.parse_args()
    sourcefn = args.source
    targetfn = args.target

    sourcebible = load_bible(sourcefn)
    targetbible = load_bible(targetfn)

    verseids = shared_verseids(sourcebible, targetbible)
    lemmas, surface = collect_shared_verses(sourcebible, targetbible, verseids,
                                            tokenize=args.tokenize,
                                            lowercase=args.lowercase,
                                            lemmatize=args.lemmatize)
    if args.lemmatize:
        with open(args.out, "w") as outfile:
            for line in lemmas:
                print(line, file=outfile)
        with open(args.out + ".surface", "w") as outfile:
            for line in surface:
                print(line, file=outfile)
    else:
        with open(args.out, "w") as outfile:
            for line in surface:
                print(line, file=outfile)

if __name__ == "__main__": main()