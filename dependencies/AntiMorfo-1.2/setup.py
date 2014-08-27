#!/usr/bin/env python3

import sys

from distutils.core import setup

setup(name='AntiMorfo',
      version='1.2',
      description='Análisis y generación morfológica',
      author='Michael Gasser',
      author_email='gasser@cs.indiana.edu',
      url='http://www.cs.indiana.edu/~gasser/Research/software.html',
      license="GPL v3",
      packages=['l3', 'l3.morpho'],
      package_data = {'l3': ['FST/*.fst', 'Data/Es/*.txt',
                             'FST/Es/*.fst', 'FST/Es/*.lex', 'FST/Es/*.cas',
                             'FST/Qu/*.fst', 'FST/Qu/*.lex', 'FST/Qu/*.cas']}
     )
