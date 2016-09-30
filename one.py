#!/usr/bin/python

#####Lists#####
#lists are the same as arrays in perl
#as in perl they are 0-based
#a = []
#for i in range(0,6):
#    a.append(raw_input("Give me a number: "))

#for i in range(0,6):
#    print a[i]


#string concatenation: + is equivalent to . in perl 
#s=5
#q="5"
#print(s+s)
#print(q+q)

#lists can contain lists
#a=[5,10,[1,2,3]]

#to test if something is defined(similar to grep{$_ eq "string"} @a)
#print(5 in a)

#dictionary = perl s hash. still has keys and values
D = {}
D['ATG'] = "Met"
D['TAG'] = "Stop"

for d in D.itervalues():
    print(d)

a = []

for i in range(0,3):
    a.append(i)

for i in a:
    print i

x, z, v = a
print(x)


