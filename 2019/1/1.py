#!usr/bin/python

import math

def fuel_needed(mass):
    return math.floor(mass/3) - 2

answer = 0

with open('input.txt') as f:
    for line in f.readlines():
        answer += fuel_needed(int(line.strip('\n')))

print('%s\n' % (answer, ))

