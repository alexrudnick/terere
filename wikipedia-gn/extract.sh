#!/bin/bash

python WikiExtractor.py < gnwiki-latest-pages-articles.xml 
cat AA/wiki_* > plaintext.txt
