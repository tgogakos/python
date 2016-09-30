#!/usr/bin/python
import sys
import operator
from fasta2 import read_fasta

x = read_fasta(sys.argv[1])

gc_d = {}

for a,b in x.iteritems():
    gc = b.count('G') + b.count('C')
    size = len(b)
    gc_d[a]= float(gc)/size


#for line in x :
#    print line+":",x[line]

for x in gc_d:
    print x+"\t",gc_d[x]

#y = max(gc_d.iteritems(), key = operator.itemgetter(1))[1]

#for a in gc_d:
#    if gc_d[a] == y:
#        print a,"\n",gc_d[a]*100



#gc = dna.count('G') + dna.count('C')
#total = len(dna)
#gc_per = float(gc)/total

#print gc,total,gc_per




