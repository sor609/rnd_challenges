#!/usr/bin/python

# variable length banner
import sys
from __builtin__ import len

bannertxt = raw_input("Enter text: ")

numch = len(bannertxt) + 4

print "*" * numch
print "* %s *" % bannertxt
print "*" * numch