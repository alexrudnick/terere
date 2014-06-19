#!/usr/bin/env python3

"""Get you some bible text."""

import sys
from collections import defaultdict

from bs4 import BeautifulSoup

import booknames
import util

def tag_is_verse(tag):
    if tag.has_attr('class') and 'content' in tag['class']:
        if (tag.parent.has_attr('data-usfm')
            and tag.parent.has_attr('class')
            and 'verse' in tag.parent['class']):
            return True
    return False

def extract_verses(fn):
    """Given a filename, return a list of verse tuples."""
    out = defaultdict(list)

    with open(fn) as infile:
        html = infile.read()
    soup = BeautifulSoup(html)
    verse_spans = soup.find_all(tag_is_verse)
    for verse in verse_spans:
        verseid = verse.parent['data-usfm']
        text = verse.get_text()
        out[verseid].append(text)
    return out

def fix_verseid(verseid, versetext):
    if verseid.count('.') != 2:
        util.dprint("{0}\t{1}".format(verseid, versetext))
        return None
    book, chapter, verse = verseid.split(".")
    book = booknames.code(book)
    assert book in booknames.knownbooks()
    return "{0}_{1}_{2}".format(book,chapter,verse)

def main():
    fns = sys.argv[1:]
    for fn in fns:
        versetable = extract_verses(fn)
        for verseid in versetable:
            versetext = " ".join(versetable[verseid])
            verseid = fix_verseid(verseid, versetext)
            if verseid:
                print("{0}\t{1}".format(verseid, versetext))

if __name__ == "__main__": main()
