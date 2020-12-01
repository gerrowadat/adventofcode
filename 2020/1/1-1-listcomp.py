#!/usr/bin/python

# Brute force and ignorance bai.

import sys

with open(sys.argv[1]) as f:
  lines = f.readlines()

numbers = []

for l in lines:
  numbers.append(int(l.strip('\n')))

snums = sorted(numbers)

# ok, slightly refined brute force.

messy_result = [[snums[x] for x in range(0, len(snums)) if snums[x] + snums[y] == 2020 ] for y in range(0, len(snums))]

clean_result = [x for x in messy_result if x]

print('%d * %d == %d' % (clean_result[0][0], clean_result[1][0], (clean_result[0][0] * clean_result[1][0])))


