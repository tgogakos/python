#!/usr/bin/python

import itertools

def main():
    number = raw_input("enter number: ")
    number = int(number)
    mylist = list(range(1,number+1))
    perms = list(itertools.permutations(mylist, number))
    
    for y in perms:
        for z in y:
            print z,
        print

    print perms
    
    total = 0
    for x in perms:
        total += 1
    print total
    
         

if __name__ == "__main__":
    main()
                 
