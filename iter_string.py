#!/usr/bin/python

string = 'ATGCGTAC'
target = 'ATGCGTACAAAAAA'
mers = []

for i in range(0, len(string)):
    for k in range(0, len(string)-i):
        x = string[i:(len(string)-k)]
        if x not in mers:
            mers.append(x)

mers_sorted = sorted(mers,key = len, reverse = True)

for x in mers_sorted:
    if x in target:
        print x
        break

