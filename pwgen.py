#!/usr/bin/python
#
# Random password generator - simple
#

import random, string

n = int(raw_input("Enter password length [0-32]> "))

s = ''.join(random.SystemRandom().sample(string.ascii_letters+string.digits, n))

print s
