#!/usr/bin/env python3

import fileinput

for line in fileinput.input():
    for token in line.split():
        print(token)
    print()
