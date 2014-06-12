import sys

DPRINT=True
def dprint(*a,**aa):
    if DPRINT:
        print(file=sys.stderr, *a, **aa)
