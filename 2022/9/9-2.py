#!/usr/bin/env python

import sys

class Position(object):
    def __init__(self, x=0, y=0):
        self._x = x
        self._y = y

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y


class End(object):
    def __init__(self):
        self._pos = Position(0,0)
        self._visited = set()

    @property
    def pos(self):
        return self._pos

    def set_pos(self, x, y):
        self._pos = Position(x, y)
        self._visited.add((x, y))

    def visited(self):
        return self._visited

    def move_toward(self, p):
        # move toward another 'end'

        if self.pos == p.pos:
            return

        # Straight moves.
        if self.pos.x == p.pos.x:
            if self.pos.y - p.pos.y > 1:
                self.set_pos(self.pos.x, self.pos.y - 1)
            elif p.pos.y - self.pos.y > 1:
                self.set_pos(self.pos.x, self.pos.y + 1)
        elif self.pos.y == p.pos.y:
            if self.pos.x - p.pos.x > 1:
                self.set_pos(self.pos.x -1, self.pos.y)
            elif p.pos.x - self.pos.x > 1:
                self.set_pos(self.pos.x + 1, self.pos.y)
        else:
            # Diagonal move, if necessary.
            x_offset = abs(self.pos.x - p.pos.x)
            y_offset = abs(self.pos.y - p.pos.y)
            if x_offset > 1 or y_offset > 1:
                new_x = self.pos.x
                new_y = self.pos.y
                # Move both x and y toward p
                if self.pos.x > p.pos.x:
                    new_x = self.pos.x - 1
                else:
                    new_x = self.pos.x + 1
                if self.pos.y > p.pos.y:
                    new_y = self.pos.y - 1
                else:
                    new_y = self.pos.y + 1
                self.set_pos(new_x, new_y)

def print_grid(ends):
    grid = ''
    for i in range(19, -1, -1):
        for j in range(20):
            nc = '.'
            for e in ends:
                if ends[e].pos.x == j and ends[e].pos.y == i:
                    nc = '%d' % (e, )
            grid += nc
        grid += '\n'

    print(grid)


def main():
    filename = sys.argv[1]
    with open(filename) as f:
        lines = f.readlines()

    ends = {}

    for i in range(10):
        ends[i] = End()
        ends[i].set_pos(0,0)

    for l in lines:
        print(l)
        (direction, steps) = l.strip().split()
        for s in range(int(steps)):
            if direction == 'R':
                ends[0].set_pos(ends[0].pos.x+1, ends[0].pos.y)
            elif direction == 'L':
                ends[0].set_pos(ends[0].pos.x-1, ends[0].pos.y)
            elif direction == 'U':
                ends[0].set_pos(ends[0].pos.x, ends[0].pos.y+1)
            elif direction == 'D':
                ends[0].set_pos(ends[0].pos.x, ends[0].pos.y-1)

            for i in range(1, 10):
                ends[i].move_toward(ends[i-1])
        print_grid(ends)


    print len(ends[9].visited())


if __name__ == '__main__':
    main()
