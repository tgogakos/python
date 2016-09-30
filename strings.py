#!/usr/bin/python
from sys import argv
import math
import re

class Employee:
    "this is a test class"
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def displayCount(self):
        print "total {}".format(self.empCount)
    
    def displayEmployee(self):
        print self.name, self.salary, self.age

    
emp1 = Employee('tasos', 10)
emp2 = Employee('giulia', 20)
emp3 = Employee('c', 23)

emp1.age = 7
emp1.displayEmployee()
emp1.displayCount()
emp2.displayCount()
print Employee.empCount
#print emp1.age
#print Employee.__dict__
#print Employee.__doc__
#print Employee.__module__
#print Employee.__name__
#print Employee.__bases__
"""
class A:
    def __init__(self):
        print "A"

class B(A):
   def __init__(self):
        print "B"

#print B.__bases__

print issubclass(A,B)
print isinstance(emp2, Employee)    
class Vector:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return 'vector {} {}'.format(self.a,self.b)

    def __add__(self, other, other):
        return Vector(self.a + other.a , self.b + other.b)

v1 = Vector(2,10)
v2 = Vector(3,3)
v3 = Vector(5,5)
print v1 + v2 + v3
"""

line = "cats are smarter than dogs"
matchObj = re.match(r'(.*) are (.*?) .*', line, re.M|re.I)

print matchObj.group()
