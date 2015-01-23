#!/usr/bin/env python3

"""Lemmatize you some pre-tokenized text, with one sentence per line!

The text must be in Quechua or Guarani. English and Spanish should get run
through FreeLing instead.
"""

import os
import sys

## MA for gn and qu
here = os.path.dirname(os.path.realpath(__file__))
paramorfo = os.path.realpath(
    os.path.join(here, "..", "dependencies", "ParaMorfo-1.1"))
sys.path.append(paramorfo)
antimorfo = os.path.realpath(
    os.path.join(here, "..", "dependencies", "AntiMorfo-1.2"))
sys.path.append(antimorfo)
import l3
import antimorfo

LANGUAGES = "gn qu".split()

def analyze(lang, word):
    """Return either a morphological analysis of the word, or if we can't do
    that, just the surface form again. Only do this for qu and gn."""
    ## XXX: speed hack: don't lemmatize ever.
    ## return ("lemma:" + word)
    if "qu" == lang:
        analyses = antimorfo.anal_word("qu", word, raw=True)
    else:
        analyses = l3.anal(lang, word, raw=True)
    ## remove Nones from the list? ...
    analyses = [a for a in analyses if (a and a[0])]
    if not analyses:
        return word
    ## XXX: really we want morphological disambiguation here; is the first
    ## analysis the most likely? Probably they're unordered.
    lemmas = sorted(set(a[0] for a in analyses))
    return "/".join(lemmas)

def analyze_sentence(lang, words):
    """Given a list of words (like a sentence or a bible verse), return the list
    of the lemmatized forms of those words."""

    ## not English, just run the MA
    lemmas = []
    for w in words:
        try:
            lemmas.append(analyze(lang, w))
        except:
            assert False, "failed to analyze: {0}".format(w)
    return lemmas

def main():
    lang = sys.argv[1]
    infn = sys.argv[2]
    outfn = sys.argv[3]
    annotatedfn = outfn + ".annotated"
    assert lang in LANGUAGES, "need to specify target language in fn"

    ## warm up the morphological analyzers in the right order
    if lang == "gn":
        l3.anal_word("gn", "terere", raw=True)
    if lang == "qu":
        antimorfo.anal_word("qu", "qallariypin", raw=True)
    print("OK DONE LOADING MA")

    with open(infn) as infile, open(outfn, "w") as outfile:
        for line in infile:
            targetwords = line.split()
            targetlemmas = analyze_sentence(lang, targetwords)
            right = " ".join(targetlemmas)
            print(right, file=outfile)

if __name__ == "__main__": main()
