#!/usr/bin/python3

with open("input.txt") as f:
    lines = [x.strip('\n') for x in f.readlines()]

result = 0

for l in lines:
    nums = sorted([int(x) for x in l.split('\t')])
    result += (nums[-1] - nums[0])

print(result)
