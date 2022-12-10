#!/usr/bin/env python

import sys

class Display(object):
    def __init__(self):
        self._clock = 0
        self._x = 1
        self._signal_hist = {}

    def _record_signal(self):
        print('[%d] [x: %d] %d' % (self._clock, self._x, self.signal()))
        self._signal_hist[self._clock] =  self.signal()

    def signal_at_clock(self, clock):
        return self._signal_hist[clock]


    def signal(self):
        return self._clock * self._x

    def noop(self):
        self._clock += 1
        self._record_signal()

    def add_x(self, num):
        self._clock += 1
        self._record_signal()
        self._clock += 1
        self._record_signal()
        self._x += num


def main():
    filename = sys.argv[1]
    with open(filename) as f:
        lines = f.readlines()

    d = Display()

    for l in lines:
        l = l.strip()
        print(l)
        if l == 'noop':
            d.noop()
        else:
            (inst, op) = l.split()
            d.add_x(int(op))

    cycles = [20, 60, 100, 140, 180, 220]
    tot = 0
    for c in cycles:
        print ('[%d] %d' % (c, d.signal_at_clock(c)))
        tot += d.signal_at_clock(c)

    print('sum %d' % (tot,))


if __name__ == '__main__':
    main()
