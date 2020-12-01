#!/usr/bin/python

# Brute force and ignorance bai.

import sys

with open(sys.argv[1]) as f:
  lines = f.readlines()

numbers = []

for l in lines:
  numbers.append(int(l.strip('\n')))

# ok, slightly refined brute force.

for i in range(0, len(numbers)):
  for j in range(0, len(numbers)):
    if numbers[i] + numbers[j] == 2020:
      print ('%d + %d == 2020 (product: %d)' % (numbers[i], numbers[j], (numbers[i] * numbers[j])))
      sys.exit(0)
