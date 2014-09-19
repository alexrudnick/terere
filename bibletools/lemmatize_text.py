#!/usr/bin/env python3

"""
Lemmatize you some text!
"""

import sys

from lemmatize_bitext import analyze_sentence
from lemmatize_bitext import LANGUAGES

from lemmatize_bitext import l3
from lemmatize_bitext import antimorfo

def main():
    sl = sys.argv[1]
    infn = sys.argv[2]
    outfn = sys.argv[3]
    assert sl in LANGUAGES, "need to specify source language in fn"

    ## warm up the morphological analyzers in the right order
    if "es" == sl:
        l3.anal_word("es", "cargando", raw=True)
    if "gn" == sl:
        l3.anal_word("gn", "terere", raw=True)
    if "qu" == sl:
        antimorfo.anal_word("qu", "qallariypin", raw=True)
    print("OK DONE LOADING MA")

    with open(infn) as infile, open(outfn, "w") as outfile:
        for line in infile:
            left = line.strip()
            sourcewords = left.split()
            sourcelemmas = analyze_sentence(sl, sourcewords)
            left = " ".join(sourcelemmas)
            print(left, file=outfile)

if __name__ == "__main__": main()
