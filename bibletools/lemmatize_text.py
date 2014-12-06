#!/usr/bin/env python3

"""Lemmatize you some pre-tokenized text, with one sentence per line!

The text must be in Quechua or Guarani or English.
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

LANGUAGES = "en gn qu".split()

## MA for en
import nltk
wnl = nltk.stem.WordNetLemmatizer()

def analyze(lang, word):
    """Return either a morphological analysis of the word, or if we can't do
    that, just the surface form again. Also return what we think its pos tag
    is. Only do this for qu and gn."""

    assert lang in ["qu", "gn"] ## need to run pos tagger on English sentences

    ## XXX: speed hack: don't lemmatize ever.
    return ("lemma:" + word, "thisisthetag")

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

    postags = sorted(set(a[1]['pos'] for a in analyses))
    print(postags)

    return "/".join(lemmas)

VERBS = "MD VB VBD VBG VBN VBP VBZ".split()
NOUNS = "NN NNS NNP NNPS".split()
ADJECTIVES = "JJ JJR JJS".split()

def analyze_sentence(lang, words):
    """Given a list of words (like a sentence or a bible verse), return the list
    of the lemmatized forms of those words."""

    if "en" == lang:
        tagged = nltk.pos_tag(words)
        tags = [tag for word,tag in tagged]
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
    lemmas = []
    for w in words:
        lemma, tag = analyze(lang, w) 
        lemmas.append(lemma)
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
