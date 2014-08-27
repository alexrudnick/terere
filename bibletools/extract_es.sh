#!/bin/bash

## Note that for getting the Spanish RVR version, use the spidered one, not the
## one from Rada's group. The unicode is a little mussed up on Rada's RVR.

./flatten_spanish_rvr95.sh > es.bible

## alternative Spanish translation; try both probably
# flatten_spanish_tla.sh > es.bible
