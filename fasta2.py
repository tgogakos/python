#!/usr/bin/python

def read_fasta(x):
    seqs={}
    name= ''
    file = open(x, "r")
    for line in file:
        line = line.rstrip("\n")
        if line[0] == ">":
            name = line[1:]
            seqs[name]=''
        else:
            seqs[name]= seqs[name] + line
            
          
#    for x in seqs:
#        print x+":",seqs[x]
            
    return seqs        
#if __name__=="__main__":
#    main()
