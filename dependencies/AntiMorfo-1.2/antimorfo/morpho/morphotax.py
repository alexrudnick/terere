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
-------------------------------------------------------
Morphotactic FSTs.
"""

import re, os

## Regexs for parsing Morphotaxes
# A new morpheme slot specification (or all)
slot_re = re.compile(r'\s*(\S+):')
# Name of a lexicon file: +file+
lex_re = re.compile(r'\+(\S+)\+')
# Beginning of a set of alternatives: either label [fss]
either_re = re.compile(r'\s*either\s+(\S+)\s*(.*?)$')
# Further alternative: or label [fss]
or_re = re.compile(r'\s*or\s+(\S+)\s*(.*?)$')
# Next slot: then label [fss]
then_re = re.compile(r'\s*then\s+(\S+)\s*(.*?)$')
# Next slot and the beginning of an alternative
theneither_re = re.compile(r'\s*then\s+either\s+(\S+)\s*(.*?)$')

class Morphotax:

    def __init__(self, label='', cascade=None):
        self.label = label
        self.cascade = cascade
        self.slot_dict = {}
        self.slots = []

    @staticmethod
    def load(filename, cascade=None, seg_units=[], verbose=False):
        """
        Load a Morphotax from a file. Morphotax files end in .mtax.
        """
        if verbose:
            print('Loading Morphotax from', filename)
        directory, fil = os.path.split(filename)
        label, suffix = fil.split('.')
        
        # Assume the file exists
        stream = open(filename, encoding='utf-8')
        lines = stream.read().split('\n')[::-1]

        morphotax = Morphotax(label=label, cascade=cascade)

        # Accumulate current slots for this sequence
        slots = []
        # Accumulate current alternatives for a particular position
        alternatives = set()
        # Label for the current slot sequence
        label = ''

        while lines:
            
            # Get a line, stripping off comments
            line = lines.pop().split('#')[0].strip()

            print('slots', slots)
            print('line', line)

            # Line might be blank or only have comments
            if not line: continue

            # Try matching line against various regexs

            # Name of a new morpheme sequence or all
            m = slot_re.match(line)
            if m:
                if slots:
                    # There's a current slot sequence, so record it
                    if label == 'all':
                        morphotax.slots = slots
                    else:
                        morphotax.slot_dict[label] = slots
                    slots = []
                # New morpheme sequence
                label = m.group(1)
                continue

            # Name of the first of a set of alternative slots
            m = either_re.match(line)
            if m:
                slot, fss = m.groups()
                if slot is None: raise ValueError('bad either line: {0}'.format(line))
                alternatives = {(slot, fss)}
                continue

            # Name of a further alternative slot
            m = or_re.match(line)
            if m:
                slot, fss = m.groups()
                if slot is None: raise ValueError('bad or line: {0}'.format(line))
                alternatives.add((slot, fss))
                continue

            # Next slot in the sequence begins with an alternative
            m = theneither_re.match(line)
            if m:
                # If there's a current set of alternatives, add it to the sequence
                if alternatives:
                    slots.append(alternatives)
                    alternatives = set()
                if slot is None: raise ValueError('bad then either line: {0}'.format(line))
                # Start a new set of alternatives
                slot, fss = m.groups()
                alternatives = {(slot, fss)}
                continue

            # Name of the next slot in the sequence
            m = then_re.match(line)
            if m:
                # If there's a current set of alternatives, add it to the sequence
                if alternatives:
                    slots.append(alternatives)
                    alternatives = set()
                if slot is None: raise ValueError('bad then line: {0}'.format(line))
                # Add the new slot to the sequence
                slot, fss = m.groups()
                slots.append((slot, fss))
                continue

            raise ValueError("bad line: {0}".format(line))

        if alternatives:
            slots.append(alternatives)
        if slots:
            if label == 'all':
                morphotax.slots = slots
            else:
                morphotax.slot_dict[label] = slots

        return morphotax

class Morpheme:
    pass
