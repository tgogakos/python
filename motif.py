#!/usr/bin/python
import sys
#import operator
from fasta2 import read_fasta
from search import les

x = sys.argv[1]
seqs = read_fasta(x)
data = {}
mers = []
sequences = []

for x in seqs:
    data[x]={}
    data[x]['sequence']=seqs[x]
    data[x]['length']=len(seqs[x])
    sequences.append(data[x]['sequence'])
    
for x in sorted(data, key = lambda x:data[x]['length'], reverse= True):
    for i in range(0, data[x]['length']-1):
        for k in range(0,data[x]['length']-i):
            new = data[x]['sequence'][i:data[x]['length']-k]
            if les(new, sequences):
                mers.append(new)

print sorted(mers, key =len,  reverse= True)[0]


                




    
