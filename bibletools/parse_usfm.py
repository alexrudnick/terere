#!/usr/bin/env python3

"""
Script to pull easily alignable text out of the USFM format used by the World
English Bible. Apparently this USFM format is widely used, so this may be useful
in other contexts too.

Output format is one verse per line, like this:
BOOK_chapter_verse{TAB}Text of verse goes here.
"""

import fileinput
import re
import sys

import booknames
import util


FOOTNOTE_PATTERN = re.compile(r"\\f .*?\\f[*]")
START_FOOTNOTE_PATTERN = re.compile(r"\\f")
def remove_footnotes(book, chapter, verse, text):
    """Heavy-handedly use a regex to remove footnotes. Returns a new string."""
    out = re.sub(FOOTNOTE_PATTERN, "", text)
    if out == text:
        if re.search(START_FOOTNOTE_PATTERN, text):
            util.dprint("not good -- start of footnote but no end?")
            util.dprint(text)
            util.dprint(chapter, verse, text)
            assert False
    return out

CROSSREF_PATTERN = re.compile(r"\\x .*?\\x[*]")
START_CROSSREF_PATTERN = re.compile(r"\\x")
def remove_crossrefs(book, chapter, verse, text):
    """Heavy-handedly use a regex to remove cross-references. Returns a new
    string."""
    out = re.sub(CROSSREF_PATTERN, "", text)
    if out == text:
        if re.search(START_CROSSREF_PATTERN, text):
            util.dprint("not good -- start of crossref but no end?")
            util.dprint(text)
            util.dprint(chapter, verse, text)
            assert False
    return out

TOREMOVE = "\\wj* \\wj \\nb \\li \\p \\q2 \\q \\b \\m".split()
def remove_formatting(book, chapter, verse, text):
    """Given the text of a verse, strip out the USFM formatting markers."""
    out = text
    for toremove in TOREMOVE:
        out = out.replace(toremove, "")
    return out

SPEAKER_PATTERN = re.compile(r"\\sp [\w]+")
def remove_speaker_annotations(book, chapter, verse, text):
    """Given the text of a verse, take out the \\sp SPEAKER annotations."""
    out = re.sub(SPEAKER_PATTERN, "", text)
    if out != text:
        matched = re.search(SPEAKER_PATTERN, text)
        speaker = matched.group(0)
        util.dprint("Stripped speaker identification: '{0}' in '{1}'".format(
            speaker, (chapter,verse,text)))
    return out


## NOTE: USFM doesn't require that verses be all on one line in the input file.
## We're going to have to merge lines as we go.
## The interesting thing here is -- when do we know when we're at the end of a
## verse?

def clean_and_print(book, chapter, verse, text):
    fixed = remove_footnotes(book, chapter, verse, text)
    fixed = remove_crossrefs(book, chapter, verse, fixed)
    fixed = remove_formatting(book, chapter, verse, fixed)
    fixed = remove_speaker_annotations(book, chapter, verse, fixed)
    fixed = fixed.strip()
    if fixed:
        print("{0}_{1}_{2}\t{3}".format(book, chapter, verse, fixed))

def main():
    seenbooks = set()
    book = None
    chapter = None
    verse = None
    text = ""

    for bookfn in sys.argv[1:]:
        with open(bookfn) as infile:
            for line in infile:
                line = line.strip()
                # print("LINE", line)
                if any(line.startswith(startmarker)
                       for startmarker in ["\\v", "\\h", "\\c", "\\d"]):
                    if book and chapter and verse and text:
                        clean_and_print(book, chapter, verse, text)
                        text = ""
                    if book and chapter and text and (verse is None):
                        util.dprint("skipping structure information:", text)
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
                    elif line.startswith("\\d"):
                        splitted = line.split(maxsplit=1)
                        verse = None
                        text = splitted[1]
                        continue
                else:
                    text = text + " " + line
            ## hit the end of this file.
            if book and chapter and verse and text:
                clean_and_print(book, chapter, verse, text)
            book = None
            chapter = None
            verse = None
            text = ""


    util.dprint("Saw this many books out of expected 66:",len(seenbooks))
    util.dprint("books we haven't seen:", booknames.knownbooks() - seenbooks)

if __name__ == "__main__": main()
