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

    for l in lines:
        l = l.strip()
        cp1 = l[:len(l)/2]
        cp2 = l[len(l)/2:]
        common = [x for x in cp2 if x in cp1][0]
        print('1 %s 2 %s com %s' % (cp1, cp2, common))
        prio_sum += prio(common)

    print('%d' % (prio_sum))


if __name__ == '__main__':
    main()
