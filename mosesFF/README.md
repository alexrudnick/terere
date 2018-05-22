To install the Chipa feature function in your copy of Moses, link these two
files into /path/to/mosesdecoder/moses/FF.

Like so:

  $ cd ~/mosesdecoder/moses/FF
  $ ln -s ~/terere/mosesFF/ChipaFF.h .
  $ ln -s ~/terere/mosesFF/ChipaFF.cpp .

Also edit your ~/mosesdecoder/moses/FF/Factory.cpp to include the lines:
  #include "moses/FF/ChipaFF.h"
  ...

  MOSES_FNAME(ChipaFF);

... then rebuild Moses.

  $ cd ~/mosesdecoder
  $ ./compile.sh --clean
  $ ./compile.sh
