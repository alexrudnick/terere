Before proceding, make sure you have libcurl installed!

  $ sudo aptitude install libcurl4-openssl-dev

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


Also you'll need to install a newer version of the xmlrpc library into your
moses installation. Use the provided shell script, like so. NB: check the paths
in that shell script first, to reflect your installation!

  $ cd ~/terere/mosesFF
  $ ./install_xmlrpc.sh


... then rebuild Moses.

  $ cd ~/mosesdecoder
  $ ./compile.sh --clean
  $ ./compile.sh
