#!/usr/bin/env python3

"""Get you some bible text. This works on HTML downloaded from the mobile
version of YouVersion, which is sadly no longer with us."""

import sys
from bs4 import BeautifulSoup

def tag_is_verse(tag):
    return (tag.name == "span" and
            tag.has_key("class") and
            "verse" in tag["class"])

def extract_verses(fn):
    """Given a filename, return a list of verse tuples."""
    out = []

    with open(fn) as infile:
        html = infile.read()
        html = html.replace("</span>", " </span>")
        html = html.replace("</div>", " </div>")
    soup = BeautifulSoup(html)
    verse_spans = soup.find_all(tag_is_verse)
    for verse in verse_spans:
        text = verse.get_text()

        assert "\xa0" in text
        splitted = text.split("\xa0", 1)
        versenum = splitted[0]
        tokens = splitted[1].strip().split()
        text = " ".join(tokens)

        assert(verse.has_key('id'))
        verseid = verse['id']
        assert verseid.endswith("_" + versenum)

        out.append((verseid, text))
    return out

def main():
    fns = sys.argv[1:]
    for fn in fns:
        verse_pairs = extract_verses(fn)
        for verseid, versetext in verse_pairs:
            print("{0}\t{1}".format(verseid, versetext))

if __name__ == "__main__": main()
