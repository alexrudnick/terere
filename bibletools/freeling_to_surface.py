#!/usr/bin/env python3

"""
Takes a freeling-analyzed file and produces the source-side as tokenized surface
text; prints it to stdout.

python3 freeling_to_surface.py \
    --freeling bible.es-en.source.freeling > bible.es-en.surface
"""

import argparse

def get_argparser():
    parser = argparse.ArgumentParser(description='freeling_to_surface')
    parser.add_argument('--freeling', type=str, required=True)
    return parser

def main():
    parser = get_argparser()
    args = parser.parse_args()

    with open(args.freeling) as infile:
        tokens = []
        lineno = 0
        for line in infile:
            lineno += 1
            line = line.strip()
            if tokens and not line:
                print(" ".join(tokens))
                tokens = []
                continue
            # sirvan servir VMSP3P0 0.885892
            try:
                ## There can actually be more than the first four fields.
                ## But we just take the first four.
                surface, lemma, tag, confidence = line.split()[:4]
                tokens.append(surface)
            except:
                print("surprising line:", line, lineno)
                break

if __name__ == "__main__": main()
