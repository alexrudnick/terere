#!/usr/bin/env python3

verse_gen_4_1 = "The man knew\\f + or, lay with, or, had relations with\\f* Eve his wife. She conceived,\\f + or, became pregnant\\f* and gave birth to Cain, and said, “I have gotten a man with Yahweh’s help.”"
verse_gen_4_1_nofootnote = "The man knew Eve his wife. She conceived, and gave birth to Cain, and said, “I have gotten a man with Yahweh’s help.”"

verse_kgs_12_4 = "Jehoash said to the priests, “All the money of the holy things that is brought into Yahweh’s house, in current money, the money of the people for whom each man is evaluated,\\x + \\+zref \\+ztgt EXO.30.12 \\+ztgt*\\+zref*Exodus 30:12\\+zrefend \\+zrefend*\\x* and all the money that it comes into any man’s heart to bring into Yahweh’s house,"
verse_kgs_12_4_nocrossref = "Jehoash said to the priests, “All the money of the holy things that is brought into Yahweh’s house, in current money, the money of the people for whom each man is evaluated, and all the money that it comes into any man’s heart to bring into Yahweh’s house,"

import unittest

import parse_usfm

class TestCleanup(unittest.TestCase):
    def setUp(self):
        self.seq = list(range(10))

    def test_footnotes_gen_4_1(self):
        """The problem here was that we were doing greedy regex matches. We
        consider both footnotes to be part of one *big* footnote, but that's
        wrong."""
        cleaned = parse_usfm.remove_footnotes("GEN", 4, 1, verse_gen_4_1)
        self.assertEqual(cleaned, verse_gen_4_1_nofootnote)

    def test_crossref_kgs_12_4(self):
        cleaned = parse_usfm.remove_crossrefs("KGS", 12, 4, verse_kgs_12_4)
        self.assertEqual(cleaned, verse_kgs_12_4_nocrossref)

    def test_speaker(self):
        cleaned = parse_usfm.remove_speaker_annotations("foo", 0, 0,
            "does this even work \\sp Speakername Maybe.")
        cleaned = cleaned.replace("  ", " ")
        self.assertEqual(cleaned, "does this even work Maybe.")

if __name__ == '__main__':
    unittest.main()


