#!/usr/bin/env python

import sys
import os
import re

# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # split the line into words
    fileName = os.environ['/mnt/f/Academia/Teaching/CS4417B/Last Year/A2/test.txt']
    words = line.split()
    # increase counters
    for word in words:
        # write the results to STDOUT (standard output);
        # what we output here will be the input for the
        # Reduce step, i.e. the input for reducer.py
        #
        # tab-delimited; the trivial word count is 1
         print '%s\t%s' % (fileName + ' ' + word, 1)
