#!/usr/bin/python

from sys import argv

s = argv[1]
def main():
    
    codons=[]
    k=1
    for i in range (len(s)-3, -1, -3):
        print(k, end='\t')
        w = s[i:i+3]
        codons.append(w)
        print(w)
        k+=1
        
    print(len(s))
    print('TGA' in codons)

if __name__ =="__main__":main()



