#!/usr/bin/env python3

"""
Usage: python3 one_sentence_per_line.py infile.txt outfile.txt

Take a text file, use NLTK to segment the sentences and print out one sentence
per line into the specified output file.

For consistency here, do not use NLTK's word tokenizer; we're always using the
cdec tokenizer for Guarani.
"""

import argparse
import nltk

def get_argparser():
    """Build the argument parser for main."""
    parser = argparse.ArgumentParser(description='one_sentence_per_line')
    parser.add_argument('--infn', type=str, required=True)
    parser.add_argument('--outfn', type=str, required=True)
    return parser

def main():
    parser = get_argparser()
    args = parser.parse_args()

    with open(args.infn) as infile:
        with open(args.outfn, "w") as outfile:
            for line in infile:
                line = line.strip()
                sentences = nltk.sent_tokenize(line)
                for sent in sentences:
                    sent = sent.strip()
                    if not sent: continue
                    print(sent, file=outfile)

if __name__ == "__main__": main()
