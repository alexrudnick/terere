#!/bin/bash

# Script to install the latest stable version of xmlrpc-c into your Moses
# installation.

WORKDIR=$HOME/mosesdecoder/build
MOSESOPT=$HOME/mosesdecoder/opt

mkdir -p WORKDIR
cd $WORKDIR

REPOS=http://svn.code.sf.net/p/xmlrpc-c/code/advanced
svn checkout $REPOS xmlrpc-c

cd xmlrpc-c
./configure --prefix="$MOSESOPT" --enable-cplusplus
make
make install
