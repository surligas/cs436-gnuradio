
'''
Blocks for the CS 436 lesson
'''

# The presence of this file turns this directory into a Python package
import os

try:
    from cs436_swig import *
except ImportError:
    dirname, filename = os.path.split(os.path.abspath(__file__))
    __path__.append(os.path.join(dirname, "..", "..", "swig"))
    from cs436_swig import *