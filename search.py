#!/usr/bin/python

def les(a,b):
    for x in b:
        if not a in x:
            return False
    return True
