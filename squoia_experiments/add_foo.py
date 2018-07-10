#!/usr/bin/env python3

import fileinput

for line in fileinput.input():
    line = line.strip()
    print(line)
    print("FOO")
