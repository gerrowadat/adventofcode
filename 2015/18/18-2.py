#!/usr/bin/env python

import sys


class Lights(object):
    def __init__(self, size):
        self._size = size
        self._l = []
        for i in range(size):
            self._l.append([False] * size)

    def __str__(self):
        ret = ''
        for row in self._l:
            for light in row:
                ret += '#' if light is True else '.'
            ret += '\n'
        return ret

    def light(self, x, y):
        return self._l[x][y]

    def set(self, x, y, val):
        self._l[x][y] = val

    def on(self, x, y):
        self.set(x, y, True)

    def off(self, x, y):
        self.set(x, y, False)

    def from_lines(self, raw):
        for i in range(self._size):
            for j in range(self._size):
                if raw[i][j] == '#':
                    self.on(i, j)
                elif raw[i][j] == '.':
                    self.off(i, j)
                else:
                    raise ValueError(
                            'unknown char %s in raw input' % (raw[i][j]))
        # Whoops
        self.on(0,0)
        self.on(0, self._size-1)
        self.on(self._size-1, 0)
        self.on(self._size-1, self._size-1)

    def neighbours(self, x, y):
        possibles = [
                (x-1, y-1),
                (x-1, y),
                (x-1, y+1),
                (x, y-1),
                (x, y+1),
                (x+1, y-1),
                (x+1, y),
                (x+1, y+1)
                ]
        return [x for x in possibles if (
            0 <= x[0] < self._size and 0 <= x[1] < self._size)]

    def neighbours_on(self, x, y):
        return len([x for x in self.neighbours(x, y) if (
            self.light(*x) is True)])

    def animate(self):
        new_l = []
        for i in range(self._size):
            new_l.append([False] * self._size)
        for i in range(self._size):
            for j in range(self._size):
                if self.light(i, j) is True:
                    if self.neighbours_on(i, j) in [2, 3]:
                        new_l[i][j] = True
                    else:
                        new_l[i][j] = False
                else:
                    if self.neighbours_on(i, j) == 3:
                        new_l[i][j] = True
                    else:
                        new_l[i][j] = False
        # Whoops
        new_l[0][0] = True
        new_l[0][self._size-1] = True
        new_l[self._size-1][0] = True
        new_l[self._size-1][self._size-1] = True

        self._l = new_l

    def count_lights(self):
        ret = 0
        for i in range(self._size):
            for j in range(self._size):
                if self.light(i, j) is True:
                    ret += 1
        return ret


def main():
    filename = sys.argv[1]
    with open(filename) as f:
        lines = f.readlines()

    lts = Lights(size=len(lines))

    lts.from_lines(lines)

    for _ in range(100):
        lts.animate()

    print(str(lts))
    print('There are %d lights.' % (lts.count_lights()))


if __name__ == '__main__':
    main()
