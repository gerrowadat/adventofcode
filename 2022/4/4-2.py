#!/usr/bin/env python

import sys

def overlaps(r1, r2):
    if r1[0] <= r2[0] <= r1[1]:
        return True
    if r1[0] <= r2[1] <= r1[1]:
        return True
    if r2[0] <= r1[0] <= r2[1]:
        return True
    if r2[0] <= r1[1] <= r2[1]:
        return True
    return False


def main():
    filename = sys.argv[1]
    with open(filename) as f:
        lines = f.readlines()

    ol = 0

    for l in lines:
        (e1, e2) = l.strip().split(',')
        r1 = [int(x) for x in e1.split('-')]
        r2 = [int(x) for x in e2.split('-')]
        if overlaps(r1, r2):
            ol += 1

    print('%d' % (ol, ))

if __name__ == '__main__':
    main()
