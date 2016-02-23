#!/bin/bash

# Script to install the latest stable version of xmlrpc-c and libcurl into your
# Moses installation.

WORKDIR=$HOME/mosesdecoder/build
MOSESOPT=$HOME/mosesdecoder/opt

mkdir -p WORKDIR

## Install libcurl first, so we'll have that available when we build xmlrpc.
cd $WORKDIR
wget https://curl.haxx.se/download/curl-7.47.1.tar.gz
tar xf curl-7.47.1.tar.gz
cd curl-7.47.1
./configure --prefix="$MOSESOPT"
make
make install


## Now build xmlrpc.
cd $WORKDIR
REPOS=http://svn.code.sf.net/p/xmlrpc-c/code/advanced
svn checkout $REPOS xmlrpc-c

cd xmlrpc-c
./configure --prefix="$MOSESOPT" --enable-cplusplus
make
make install


