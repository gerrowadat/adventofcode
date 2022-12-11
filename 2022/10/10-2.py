#!/usr/bin/env python

import sys

class Display(object):
    def __init__(self):
        self._clock = 0
        self._x = 1
        self._x_hist = {}
        self._record()

    def _record(self):
        self._x_hist[self._clock] =  self._x

    def x_at_clock(self, clock):
        return self._x_hist[clock]

    def noop(self):
        self._clock += 1
        self._record()

    def add_x(self, num):
        self._clock += 1
        self._record()
        self._clock += 1
        self._record()
        self._x += num


def main():
    filename = sys.argv[1]
    with open(filename) as f:
        lines = f.readlines()

    d = Display()

    for l in lines:
        l = l.strip()
        if l == 'noop':
            d.noop()
        else:
            (inst, op) = l.split()
            d.add_x(int(op))

    clock = 0
    for l in range(6):
        line = ''
        for c in range(40):
            x = d.x_at_clock(c+1+(40*l))
            spr = [x-1, x, x+1]
            if c in spr:
                line += '#'
            else:
                line += '.'
        print(line)


if __name__ == '__main__':
    main()
