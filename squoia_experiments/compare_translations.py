#!/usr/bin/env python3

import sys

def main():
    if len(sys.argv) != 4:
        print("usage: compare_translations.py source target1 target2")
        return

    source_fn = sys.argv[1]
    target1_fn = sys.argv[2]
    target2_fn = sys.argv[3]

    source_lines = []
    target1_lines = []
    target2_lines = []

    with open(source_fn) as infile:
        for line in infile:
            line = line.strip()
            source_lines.append(line)
    with open(target1_fn) as infile:
        for line in infile:
            line = line.strip()
            target1_lines.append(line)
    with open(target2_fn) as infile:
        for line in infile:
            line = line.strip()
            target2_lines.append(line)

    assert len(source_lines) == len(target1_lines), "wrong length of input"
    assert len(source_lines) == len(target2_lines), "wrong length of input"

    for src, trg1, trg2 in zip(source_lines, target1_lines, target2_lines):
        if trg1 == trg2: continue
        words1 = set(trg1.split(" "))
        words2 = set(trg2.split(" "))

        if words1 == words2: continue

        print(src)
        print(trg1)
        print("only in trg1:", words1 - words2)
        print(trg2)
        print("only in trg2:", words2 - words1)
        print()


if __name__ == "__main__": main()
