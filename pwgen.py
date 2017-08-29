#!/usr/bin/python
#
# Random password generator - simple
#

import random, string
from random import SystemRandom

print "Password generator\n"

a = int(raw_input("Enter # of letters > "))
b = int(raw_input("Enter # of digits > "))
c = int(raw_input("Enter # of special chars > "))
rnd_lett = SystemRandom().sample(string.ascii_letters,a)
rnd_digi = SystemRandom().sample(string.digits,b)
rnd_char = SystemRandom().sample(string.punctuation,c)

s = ''.join(random.sample(rnd_lett+rnd_digi+rnd_char,a+b+c))

print "\n" + s
