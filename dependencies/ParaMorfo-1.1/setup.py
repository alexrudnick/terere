#!/usr/bin/env python3

import sys

from distutils.core import setup

setup(name='ParaMorfo',
      version='1.1',
      description='Análisis y generación morfológica de castellano y guaraní',
      author='Michael Gasser',
      author_email='gasser@cs.indiana.edu',
      url='http://www.cs.indiana.edu/~gasser/Research/software.html',
      license="GPL v3",
      packages=['l3', 'l3.morpho'],
      package_data = {'l3': ['languages/es/cas/*.cas',
                             'languages/es/fst/*.fst',
                             'languages/es/lex/*.lex',
                             'languages/es/es.lg',
                             'languages/es/data/es.txt',
                             'languages/gn/cas/*.cas',
                             'languages/gn/fst/*.fst',
                             'languages/gn/lex/*.lex',
                             'languages/gn/gn.lg',
                             'languages/gn/data/escurra1.txt']}
     )
