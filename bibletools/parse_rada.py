#!/usr/bin/env python3

import re
import sys

import booknames

VERSE_PATTERN = re.compile("[[]\d+,(\d+),(\d+),(\d+)[]] (.*)")

def clean_and_print(book, chapter, verse, text):
    print("{0}_{1}_{2}\t{3}".format(book, chapter, verse, text))

def main():
    books = set()
    booknums = set()
    with open(sys.argv[1]) as infile:
        for line in infile:
            line = line.strip()
            match = re.match(VERSE_PATTERN, line)
            if match:
                book, chapter, verse, text = match.groups()
                booknums.add(int(book))
                book = booknames.booknum_to_code(book)
                books.add(book)
                text = text.strip()
                clean_and_print(book, chapter, verse, text)

if __name__ == "__main__": main()
