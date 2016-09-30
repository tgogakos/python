#!/usr/bin/python
import sys
import re

def find_max(x):
    if ("(." in x): 
        matches = re.findall("\(\.+\)", x)
        maxi =  max(matches)
        return maxi
    else:
        return 0
        
mylist=[]

with open(sys.argv[1], "r") as file:
    for line in file:
        line = line.rstrip() 
        match = find_max(line)
#        print match
        if match !=0 :
            x = int(line.index(match))
#            print x
            mylist.append(line.index(match))
    a = max(mylist)
#    print a

with open(sys.argv[1], "r") as file:
    for line in file:
        line = line.rstrip()
        match = find_max(line)
        if match != 0 :
            x = line.index(match)
            print "x"*(a-x+((a-len(match))/2))+line
        else:
            print "x"*((76-len(line))/2)+line
