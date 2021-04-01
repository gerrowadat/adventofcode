#!/usr/bin/python3

with open("input.txt") as f:
    lines = [x.strip('\n') for x in f.readlines()]

result = 0

for l in lines:
    nums = sorted([int(x) for x in l.split('\t')])
    print(nums)
    for n in nums:
        for o in [x for x in nums if x != n]:
            div = n / o
            if div.is_integer():
                result += div
                break

print(result)
