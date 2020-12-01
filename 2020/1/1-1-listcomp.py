#!/usr/bin/python

# Brute force and ignorance bai.

import sys

with open(sys.argv[1]) as f:
  lines = f.readlines()

numbers = []

for l in lines:
  numbers.append(int(l.strip('\n')))

# ok, slightly refined brute force.

result = [n for n in [[numbers[x] for x in range(0, len(numbers)) if numbers[x] + numbers[y] == 2020 ] for y in range(0, len(numbers))] if n]

print('%d * %d == %d' % (result[0][0], result[1][0], (result[0][0] * result[1][0])))


