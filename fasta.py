#!/usr/bin/perl
import sys

x = sys.argv[1]
file = open(x , "r")
seqs = {}
name = ''
for line in file:
    line = line.rstrip('\n')
    if line[0] == ">":
        name = line[1:]
        seqs[name]=''
    else:
        seqs[name]= seqs[name] + line

for x in seqs:
    print x+":",seqs[x]
