#!/bin/bash

KENLM=/space/trykenlm/kenlm/bin/lmplz

$KENLM -o 3 < gn_sentences.txt > gn.arpa
