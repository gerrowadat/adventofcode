#!/usr/bin/python3

with open("input.txt") as f:
    line = f.readline().strip('\n')

result = 0

for idx in range(0, len(line)-1):
    if line[idx] == line[idx+1]:
        result += int(line[idx])

if line[0] == line[-1]:
    result += int(line[0])

print(result)
