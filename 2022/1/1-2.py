#!/usr/bin/env python

import sys


def main():
    filename = sys.argv[1]
    with open(filename) as f:
        lines = f.readlines()

    elves = {}

    elf = 1
    elves[elf] = 0

    for i in range(len(lines)):
        if lines[i].strip() == '':
            elf += 1
            elves[elf] = 0
        else:
            elves[elf] += int(lines[i].strip())

    print sum(sorted(elves.values())[-3:])


if __name__ == '__main__':
    main()
