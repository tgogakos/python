#!/usr/bin/python

#functions
#def isprime(n):
#    if n == 1:
#        return False
#    for x in range(2,n):
#        if n % x == 0:
#            return False
#    else:
#        return True
#def primes(n=1):
#    while(True):
#        if isprime(n): yield n 
#        n += 1

#for n in primes():
#    if n > 100: break
#    print(n)

#an object is an instance of a class

##class fibonacci():
#    #constructor
#    def __init__(self, a, b):

#power 


#functions
#def main():
#    print("welcome")
#    fct(2)
#    fct(10)
#    fct()

#def fct(n=5):
#    for i in range(0,n):
#        print(i, end= " ")
#    print()

#objects. everything in python is an object
#class is the definition of an object

#class Egg:
#    #constructor
#    def __init__(self, kind = "fried"):
#        self.kind = kind
#
#    def whatKind(self):
#        return self.kind
#        #self is a reference to the object itself
#
#def main():
#    fried = Egg()
#    #cretes an object, fried, based on the class Egg
#    # the constructor is called every time a class is called
#    scrambled = Egg('scrambled')
#    print(fried.whatKind())
#    print(scrambled.whatKind())
#
#if __name__ == "__main__": main()
#

#everything in python3 is an object and has an ID, a type and a value
#ID identifies a particular instance
#type identifies the class 
#value is the content

import re

#important on object oriented programming

#inheritance

class Animal():
    def talk(self):
        print("i have smth to say")

    def walk(self):
        print("hey i m walking")

    def clothes(self):
        print("i have clothes")

#the Duck (object) inherits the attributes of Animal
class Duck(Animal):
    def __init__(self, **kwargs):
        self.variables = kwargs
 
    def set_variable(self, k, v):
        self.variables[k]=v

    def get_variable(self, k):
        return self.variables.get(k, None)
 


def main():
    donald = Duck()
    donald.set_variable("color", "vlue")
    donald.set_variable("weight", 8)
    print(donald.get_variable("color"))
    print(donald.get_variable("weight"))
    
if __name__ == "__main__":main()





