#!/usr/bin/python
import re


##count characters

#print("{} {} {} {}".format(dna.count('A'), dna.count('C'), dna.count('G'), dna.count('T')))
 ##T_to_U

def main():
    dna = raw_input("enter sequence: ")
    a = t_to_u(dna)
    b = rev_comp(dna)
    print b

    
    string = 'AAATTGAGAGAGAGAATTGAGAGAGAGAGAGAATT'
    
    for match in re.finditer("AATT", string):
        print(match.start(), match.end())


def t_to_u(x):
    x = x.replace("T", "U")
    x = x.replace("t", "u")
    return x

def rev_comp(x):
    x = x[::-1]
    revcom = ""
    for i in range(0, len(x)):
        if x[i] == "A":
            revcom +=  "T"
        if x[i] == "T":
            revcom +=  "A"
        if x[i] == "G":
            revcom +=  "C"
        if x[i] == "C":
            revcom +=  "G"
    return revcom

if __name__=="__main__":
    main()




#        dna= dna[::-1] dna
 





    


