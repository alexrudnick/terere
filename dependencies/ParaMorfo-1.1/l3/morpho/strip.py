"""
This file is part of L3Morpho.

    L3Morpho is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    L3Morpho is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with L3Morpho.  If not, see <http://www.gnu.org/licenses/>.
--------------------------------------------------------------------
Author: Michael Gasser <gasser@cs.indiana.edu>

Strip off affixes, returning stem and affixes.

"""

suffixes = {
    'selas': [('se', 'las')],
    'se': [('se',)],
    'le': [('le',)],
    'semelas': [('se', 'me', 'las')]
    }

DEACCENT = {'á': 'a', 'é': 'e', 'í': 'i', 'ó': 'o', 'ú': 'u'}
ACCENT = {'a': 'á', 'e': 'é', 'i': 'í', 'o': 'ó', 'u': 'ú'}

def accent(word, index, right=True):
    """Accent the first vowel in index position on (right) side."""
    count = 0
    segs = []
    if side:
        for pos in range(1, len(word))
            c = word[-pos]
            if c in ACCENT:
                if count == index:
                    segs.insert(0, ACCENT[c])
                else:
                    count += 1
                    segs.insert(0, c)
            else:
                segs.append(c)

def prestrip(word, prefixes):
    """word: string
    prefixes: dict with strings as keys and lists of prefixes as values.
    """
    # Start at right-end of word to prefer longer prefixes
    for n in range(1, len(word)):
        pre = word[:-n]
#        print('pre {}'.format(pre))
        if pre in prefixes:
            return word[-n:], prefixes[pre]
    return False

def sufstrip(word, suffixes):
    """
    word: string
    suffixes: dict with strings as keys and lists of suffixes as values.
    """
    # Start at the left-end to prefer longer suffixes
    for n in range(1, len(word)):
        suf = word[n:]
#        print('suf {}'.format(suf))
        if suf in suffixes:
            return word[:n], suffixes[suf]
    return False
        
