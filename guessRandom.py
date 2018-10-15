#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

secret = random.randint(1,100)
guess = int(raw_input("input a number:"))

while secret != guess:
    print "guess number is wrong"
    if guess > secret:
        print "guess number is bigger than secret"
        guess = int(raw_input("input a number:"))
    elif guess < secret:
        print "guess number is smaller than secret"
        guess = int(raw_input("input a number:"))
else:
    print "you input the right number: %s" % secret