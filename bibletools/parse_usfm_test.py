#!/usr/bin/env python3

verse_gen_4_1 = "The man knew\\f + or, lay with, or, had relations with\\f* Eve his wife. She conceived,\\f + or, became pregnant\\f* and gave birth to Cain, and said, “I have gotten a man with Yahweh’s help.”"
verse_gen_4_1_nofootnote = "The man knew Eve his wife. She conceived, and gave birth to Cain, and said, “I have gotten a man with Yahweh’s help.”"

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

if __name__ == '__main__':
    unittest.main()


