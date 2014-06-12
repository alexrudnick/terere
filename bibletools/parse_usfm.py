#!/usr/bin/env python3

"""
Script to pull easily alignable text out of the USFM format used by the World
English Bible. Apparently this USFM format is widely used, so this may be useful
in other contexts too.

Output format is one verse per line, like this:
BOOK_chapter_verse{TAB}Text of verse goes here.
"""

import fileinput

import booknames
import util

book = None
chapter = None
verse = None

seenbooks = set()

for line in fileinput.input():
    line = line.strip()
    if line.startswith("\\h"):
        splitted = line.split(maxsplit=1)
        bookname = splitted[1]
        book = booknames.code(bookname)
        if not book:
            util.dprint("warning! not a known book:", bookname)
        else:
            seenbooks.add(book)
    elif line.startswith("\\c"):
        splitted = line.split()
        chapter = splitted[1]
    elif line.startswith("\\v"):
        splitted = line.split(maxsplit=2)
        verse = splitted[1]
        text = splitted[2]
        if book and chapter and verse:
            print("{0}_{1}_{2}\t{3}".format(book, chapter, verse, text))

util.dprint("Saw this many books out of expected 66:",len(seenbooks))
util.dprint("books we haven't seen:", booknames.knownbooks() - seenbooks)
