#!/usr/bin/python
import sys
from search import les
import linecache 
import readline

x = sys.argv[1]
line2 ='GATAGATAGAA'# linecache.getline(x, 2)
f = open(x, 'r')
lines =[]
mers = []

for line in f:
    if line[0] != ">":
        line.rstrip()
        lines.append(line.rstrip())


for i in range(0, len(line2)):
    for k in range(i, len(line2)-i):
        new = line2[i:len(line2)-k+1]
        if new not in mers:

            mers.append(new)


print "-".join(mers)
                   




