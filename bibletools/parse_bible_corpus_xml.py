#!/usr/bin/env python3

"""
Script to pull easily alignable text out of XML files distributed on
https://github.com/christos-c/bible-corpus

Output format is one verse per line, like this:
BOOK_chapter_verse{TAB}Text of verse goes here.
"""

import sys
import xml.etree.ElementTree as ET

import booknames
import util

def main():
    seenbooks = set()
    book = None
    chapter = None
    verse = None
    text = ""

    for bookfn in sys.argv[1:]:
        with open(bookfn) as infile:
            root = ET.fromstring(infile.read())
            for seg in root.iter('seg'):
                seg_id = seg.get('id')
                _, book, chapter, verse = seg_id.split(".")

                book = booknames.code(book)
                if not seg.text:
                    continue

                text = seg.text.strip()
                seenbooks.add(book)

                print("{0}_{1}_{2}\t{3}".format(book, chapter, verse, text))

    util.dprint("Saw this many books out of expected 66:",len(seenbooks))
    util.dprint("books we haven't seen:",
                sorted(booknames.knownbooks() - seenbooks))
    util.dprint("surprising books:",
                sorted(seenbooks - booknames.knownbooks()))

if __name__ == "__main__": main()
