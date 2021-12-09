#!/usr/bin/env python3

class Point(object):
    def __init__(self, x, y, val):
        self._x = x
        self._y = y
        self._val = val

    def __str__(self):
        return '(%s, %s): %s' % (self.x, self.y, self.val)

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @property
    def val(self):
        return self._val

    def __eq__(self, other):
        if self.x == other.x and self.y == other.y:
            return True
        return False

    def __hash__(self):
        return hash(self.x + self.y)


class Grid(object):
    def __init__(self, xlen, ylen):
        self._g = []
        self._xlen = xlen
        self._ylen = ylen

    def __str__(self):
        ret = ''
        for i in range(self._ylen):
            for j in range(self._xlen):
                ret += self.at(j, i)
            ret += '\n'
        return ret

    def add_point(self, p):
        self._g.append(p)

    def at(self, x, y):
        return [p for p in self._g if p.x == x and p.y == y][0].val

    def neighbours(self, p):
        return [n for n in self._g if n.x in (p.x-1, p.x, p.x+1) and n.y in (p.y-1, p.y, p.y+1) and (n != p)]

    def find_low(self):
        ret = []
        for p in self._g:
            higher = [x for x in self.neighbours(p) if x.val > p.val]
            if len(higher) == len(self.neighbours(p)):
                ret.append(p)
        return ret


def main():
    with open('input.txt') as f:
        lines = [x.strip() for x in f.readlines()]

    grid = [list(y) for y in lines]

    g = Grid(len(lines[0]), len(lines))

    for y in range(len(lines)):
        for x in range(len(lines[y])):
            g.add_point(Point(x, y, grid[y][x]))


    low = g.find_low()

    print('Sum: %d' % (sum([int(v.val) for v in low]) + len(low)))


if __name__ == '__main__':
    main()
