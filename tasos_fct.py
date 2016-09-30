#!/usr/bin/python
import random

def oligo(l,n):
    total = []
    for i in range(n):
        result = ""
        for x in range(l):
            result += random.choice('ATGC')
        total.append(result)
    return total
