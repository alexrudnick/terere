#!/usr/bin/env python3

"""
python3 freeling_to_annotated.py \
    --freeling bible.es-en.source.freeling \
    --lemma_out bible.es-en.lemmas \
    --annotated bible.es-en
"""

import argparse

def get_argparser():
    parser = argparse.ArgumentParser(description='freeling_to_annotated')
    parser.add_argument('--freeling', type=str, required=True)
    parser.add_argument('--lemma_out', type=str, required=True)
    parser.add_argument('--annotated', type=str, required=True)
    return parser

def main():
    parser = get_argparser()
    args = parser.parse_args()

    with open(args.freeling) as infile, \
         open(args.lemma_out, "w") as lemmaout, \
         open(args.annotated, "w") as annotatedout:

        lemmas = []
        for line in infile:
            line = line.strip()
            if lemmas and not line:
                print(" ".join(lemmas), file=lemmaout)
                print("", file=annotatedout)
                lemmas = []
                continue
            # sirvan servir VMSP3P0 0.885892
            try:
                surface, lemma, tag, confidence = line.split()
            except:
                print("surprising line:", line)
                break
            print("{0}\t{1}\ttag={2}".format(lemma, surface, tag),
                  file=annotatedout)

if __name__ == "__main__": main()
