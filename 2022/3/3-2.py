#!/usr/bin/env python

import sys

def prio(ch):
    if 96 < ord(ch) < 123:
        return ord(ch) - 96
    elif 64 < ord(ch) < 91:
        return ord(ch) - 64 + 26
    return 0


def main():
    filename = sys.argv[1]
    with open(filename) as f:
        lines = f.readlines()

    prio_sum = 0

    for i in range(0, len(lines), 3):
        elves = lines[i:i+3]
        com = [x for x in elves[0] if x in elves[1]and x in elves[2]][0]
        prio_sum += prio(com)


    print('%d' % (prio_sum))


if __name__ == '__main__':
    main()
