To install the Chipa feature function in your copy of Moses, link these two
files into /path/to/mosesdecoder/moses/FF.

Like so:

  $ cd ~/mosesdecoder/moses/FF
  $ ln -s ~/terere/mosesFF/ChipaFF.h .
  $ ln -s ~/terere/mosesFF/ChipaFF.cpp .

... then rebuild Moses.

  $ cd ~/mosesdecoder
  $ ./compile.sh

Also, you'll need libxmlrpc for C++. Install it on Ubuntu like this:

  $ sudo aptitude install libxmlrpc-c++8-dev
