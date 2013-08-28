#!/usr/bin/env python3

"""
Usage: python3 one_sentence_per_line.py infile.txt outfile.txt

Take a text file, use NLTK to segment the sentences and tokenize the words (both
in the default NLTK way), then print out one sentence per line with the words
already tokenized, into the specified output file.
"""

import sys
import nltk

def main():
    assert len(sys.argv) == 3
    with open(sys.argv[1]) as infile:
        text = infile.read()

    sentences = nltk.sent_tokenize(text)
    with open(sys.argv[2], "w") as outfile:
        for sent in sentences:
            sent = sent.strip()
            if not sent: continue
            toks = nltk.word_tokenize(sent)
            print(" ".join(toks), file=outfile)

if __name__ == "__main__": main()
