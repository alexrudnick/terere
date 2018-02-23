#!/usr/bin/env python3

"""
python3 frog_to_lemmas.py \
    --frog europarl.es-nl.target.frog \
    --lemma_out bible.es-en.lemmas
"""

import argparse

def get_argparser():
    parser = argparse.ArgumentParser(description='frog_to_lemmas')
    parser.add_argument('--frog', type=str, required=True)
    parser.add_argument('--lemma_out', type=str, required=True)
    return parser

def main():
    parser = get_argparser()
    args = parser.parse_args()

    with open(args.frog) as infile, \
         open(args.lemma_out, "w") as lemmaout:
        lemmas = []
        lineno = 0
        for line in infile:
            lineno += 1
            line = line.strip()
            if lemmas and not line:
                print(" ".join(lemmas), file=lemmaout)
                lemmas = []
                continue
            # sirvan servir VMSP3P0 0.885892
            try:
                ## There can actually be more than the first four fields.
                ## But we just take the first four.
                index, surface, lemma = line.split('\t')[:3]
                lemmas.append(lemma)
            except:
                print("surprising line:", line, lineno)
                break

if __name__ == "__main__": main()
