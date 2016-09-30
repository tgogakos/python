#!/usr/bin/python
import sys
import random
from fasta2 import read_fasta

f = open(sys.argv[1])
lines = f.read().splitlines()
evenlines = lines[1::2]


t = sys.argv[2]
seqs = read_fasta(t)

for k in seqs:
    query = seqs[k]
    size = len(query)
    iter = int(sys.argv[3])
    pot_targ = []
    
    for l in evenlines:
        if len(l) >= size:
            pot_targ.append(l)
    
    if pot_targ:
        target = pot_targ[random.randrange(1,len(pot_targ))]
        counter = 0 
        while counter < iter:
            if size <= len(target):
                start = random.randint(0,len(target))
                if start <= size-1:
                    end = start + size
                    if end <= len(target):
                        print ">%s_%s\n%s" %(query,counter,target[start:end])
                        counter += 1
            target = pot_targ[random.randrange(1,len(pot_targ))]


