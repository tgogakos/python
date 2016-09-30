#!/usr/bin/perl
import sys
import re

string = raw_input('enter sequence ')
motif = raw_input('enter motif ')

if motif not in string:
    print "no"
else:
    for m in re.findall(motif, string, overlapped=True):
        print m


