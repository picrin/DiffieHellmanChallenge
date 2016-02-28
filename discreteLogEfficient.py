#!/bin/python
import sys

filenameWithPrime = sys.argv[1]
with open(filenameWithPrime, "r") as f:
    p = int(f.readlines()[0])

a = int(sys.argv[2])

# The generator of the group
import random
g = random.randint(0, p)

left = p
right = g

# these will be the remainder and gcd
remainder = -1
gcd = -1

reconstruct = {left: [1, 0], right: [0, 1]}

currentLeft = left
currentRight = right
counter = 0
while remainder != 0:
    remainder = currentLeft % currentRight
    counter += 1
    multiplicity = currentLeft / currentRight
    reconstructLeft = reconstruct[currentLeft]
    reconstructRight = reconstruct[currentRight]
    i = multiplicity * reconstructRight[0]
    j = multiplicity * reconstructRight[1]
    reconstruct[remainder] = [reconstructLeft[0] - i, reconstructLeft[1] - j]
    currentLeft = currentRight
    if remainder == 0:
        gcd = currentRight
    currentRight = remainder

multiplicativeInverse = (reconstruct[gcd][1] + p) % p
print (a * multiplicativeInverse)
