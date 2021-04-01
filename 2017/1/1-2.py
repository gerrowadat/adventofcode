#!/usr/bin/python3

with open("input.txt") as f:
    line = f.readline().strip('\n')

result = 0

jump = len(line) / 2

for idx in range(0, len(line)):
    cmp_idx = int((idx + jump) % len(line))
    if line[idx] == line[cmp_idx]:
        result += int(line[idx])

print(result)
