#!/usr/bin/python
#iterations of random oligos of specified length

import sys
import random

def oligo(l,n):
    total = []
    for i in range(n):
        result = ""
        for x in range(l):
            result += random.choice('ATGC')
        total.append(result)

    return total
        
if len(sys.argv) < 4:
    sys.exit("Usage: random_oligo.py <length of seq> <number of iterations>")
            
l = int(sys.argv[1])
n = int(sys.argv[2])

for x in oligo(l,n):
    print x
