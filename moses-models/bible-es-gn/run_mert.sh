#!/bin/bash

~/mosesdecoder/scripts/training/mert-moses.pl \
  bad-devset.source \
  bad-devset.target \
  "$HOME"/mosesdecoder/bin/moses \
  model/moses.ini
