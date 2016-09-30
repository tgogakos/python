#!/usr/bin/python
#shuffles lines of a file
import sys
import random

with open(sys.argv[1], 'r') as source:
    data = [ (random.random(), line) for line in source]

data.sort()

for _,line in data:
    print line.rstrip()

