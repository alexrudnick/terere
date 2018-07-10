#!/usr/bin/env python3

import fileinput

tojoin = []
for line in fileinput.input():
    line = line.strip()
    if line == "Foo nisqa":
        print(" ".join(tojoin))
        tojoin = []
    else:
        tojoin.append(line)
