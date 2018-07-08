#!/usr/bin/env python3

import fileinput

def main():
    block = []
    for line in fileinput.input():
        line = line.strip()
        if line:
            block.append(line.split())
        else:
            print(" ".join(block[0][:-1]))
            block = []

if __name__ == "__main__": main()
