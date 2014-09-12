#!/usr/bin/env python3

"""
Lemmatize you a bible in bitext format!
"""

import os
import sys

## MA for es, gn, qu
here = os.path.dirname(os.path.realpath(__file__))
paramorfo = os.path.realpath(
    os.path.join(here, "..", "dependencies", "ParaMorfo-1.1"))
sys.path.append(paramorfo)
antimorfo = os.path.realpath(
    os.path.join(here, "..", "dependencies", "AntiMorfo-1.2"))
sys.path.append(antimorfo)
import l3
import antimorfo

LANGUAGES = "en es gn qu".split()

## MA for en
import nltk
wnl = nltk.stem.WordNetLemmatizer()

def analyze(lang, word):
    """Return either a morphological analysis of the word, or if we can't do
    that, just the surface form again."""

    assert lang != "en" ## need to run pos tagger on English sentences

    analyses = []
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

VERBS = "MD VB VBD VBG VBN VBP VBZ".split()
NOUNS = "NN NNS NNP NNPS".split()
ADJECTIVES = "JJ JJR JJS".split()

def analyze_sentence(lang, words):
    """Given a list of words (like a sentence or a bible verse), return the list
    of the lemmatized forms of those words."""

    if "en" == lang:
        tagged = nltk.pos_tag(words)
        lemmas = []
        for (word, tag) in tagged:
            wntag = None
            if tag in VERBS:
                wntag = "v"
            elif tag in NOUNS:
                wntag = "n"
            elif tag in ADJECTIVES:
                wntag = "a"
            if wntag:
                lemmas.append(wnl.lemmatize(word, wntag))
            else:
                lemmas.append(word)
        assert len(words) == len(lemmas)
        return lemmas
    ## not English, just run the MA
    return [analyze(lang, w) for w in words]


def main():
    infn = sys.argv[1]
    sl, tl = infn.split(".")[1].split("-")
    assert sl in LANGUAGES, "need to specify source language in fn"
    assert tl in LANGUAGES, "need to specify target language in fn"

    ## warm up the morphological analyzers in the right order
    if "es" in [sl,tl]:
        l3.anal_word("es", "cargando", raw=True)
    if "gn" in [sl,tl]:
        l3.anal_word("gn", "terere", raw=True)
    if "qu" in [sl,tl]:
        antimorfo.anal_word("qu", "qallariypin", raw=True)
    print("OK DONE LOADING MA")

    with open(infn) as infile:
        for line in infile:
            left, right = line.split("|||")

            sourcewords = left.split()
            sourcelemmas = analyze_sentence(sl, sourcewords)
            left = " ".join(sourcelemmas)

            targetwords = right.split()
            targetlemmas = analyze_sentence(tl, targetwords)
            right = " ".join(targetlemmas)

            verseline = "{0} ||| {1}".format(left, right)
            print(verseline)

if __name__ == "__main__": main()
