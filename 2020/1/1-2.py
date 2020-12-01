#!/usr/bin/python

# Brute force and ignorance bai.

import sys

with open(sys.argv[1]) as f:
  lines = f.readlines()

numbers = []

for l in lines:
  numbers.append(int(l.strip('\n')))

sorted_nums = sorted(numbers)

# remove all refinement

for i in numbers:
  for j in numbers:
    for k in numbers:
      if i + j + k == 2020:
        print ('%d + %d + %d == %d' % (i, j, k, (i * j * k)))
        sys.exit(0)
