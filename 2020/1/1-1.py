#!/usr/bin/python

# Brute force and ignorance bai.

import sys

with open(sys.argv[1]) as f:
  lines = f.readlines()

numbers = []

for l in lines:
  numbers.append(int(l.strip('\n')))

sorted_nums = sorted(numbers)

# ok, slightly refined brute force.

for i in range(0, len(sorted_nums)):
  for j in range(len(sorted_nums)-1, 0, -1):
    if sorted_nums[i] + sorted_nums[j] == 2020:
      print ('%d + %d == 2020 (product: %d)' % (sorted_nums[i], sorted_nums[j], (sorted_nums[i] * sorted_nums[j])))
      sys.exit(0)
