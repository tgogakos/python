#!/usr/bin/python
import sys
import operator

x = sys.argv[1]
file = open(x, 'r')
file.next()
seqs ={} 

for line in file:
    fields = line.strip().split("\t")
    if fields[5] != "0" and fields[6] != "0":
        seqs[fields[0]] = fields[3]+fields[2]+fields[4]

sorted_seqs = sorted(seqs.items(), key = operator.itemgetter(0))

for k,v in sorted_seqs:
    print ">"+k+"\n"+v

