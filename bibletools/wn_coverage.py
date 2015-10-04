#!/usr/bin/env python3

import fileinput
from nltk.corpus.reader.wordnet import NOUN
from nltk.corpus import wordnet

for line in fileinput.input():
    line = line.strip().lower()
    if not line:
        continue
    lemmas = None
    for pos in ['a', 's', 'r', 'n', 'v']:
        ans = wordnet._morphy(line, pos)
        if ans:
            lemmas = ans
    if lemmas:
        print("COVERED", lemmas)
    else:
        print("NOTCOVERED", line)
