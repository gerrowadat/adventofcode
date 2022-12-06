#!/usr/bin/env python

import sys

def inside(r1, r2):
    # is r2 inside r1?
    if r2[0] >= r1[0] and r2[1] <= r1[1]:
        return True
    return False


def main():
    filename = sys.argv[1]
    with open(filename) as f:
        lines = f.readlines()

    full = 0

    for l in lines:
        (e1, e2) = l.strip().split(',')
        r1 = [int(x) for x in e1.split('-')]
        r2 = [int(x) for x in e2.split('-')]
        if inside(r1, r2) or inside (r2, r1):
            full += 1

    print('%d' % (full, ))

if __name__ == '__main__':
    main()
