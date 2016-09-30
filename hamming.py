#!/usr/bin/python
import sys
file = open(sys.argv[1], "r")
first = file.readline()
first = first.rstrip()
second = file.readline()
second = second.rstrip()
hamming = 0
    
for i in range(0,len(first)):
    if first[i] != second[i]:
        print first[i], i
        hamming += 1
            
print first
print second
print hamming

def hamming_distance(f,s):
    count = 0 
    for a,b in zip (f,s):
        if a!=b:
            count += 1
    return count
