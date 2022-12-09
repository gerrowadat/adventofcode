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

def print_grid(h, t):
    grid = ''
    for i in range(9, -1, -1):
        for j in range(10):
            if h.pos.x == j and h.pos.y == i:
                grid += 'H'
            elif t.pos.x == j and t.pos.y == i:
                grid += 't'
            else:
                grid += '.'
        grid += '\n'

    print(grid)


def main():
    filename = sys.argv[1]
    with open(filename) as f:
        lines = f.readlines()

    h = End()
    t = End()
    h.set_pos(0, 0)
    t.set_pos(0, 0)


    for l in lines:
        print(l)
        (direction, steps) = l.strip().split()
        for s in range(int(steps)):
            if direction == 'R':
                h.set_pos(h.pos.x+1, h.pos.y)
            elif direction == 'L':
                h.set_pos(h.pos.x-1, h.pos.y)
            elif direction == 'U':
                h.set_pos(h.pos.x, h.pos.y+1)
            elif direction == 'D':
                h.set_pos(h.pos.x, h.pos.y-1)

            t.move_toward(h)
        print_grid(h, t)


    print len(t.visited())





if __name__ == '__main__':
    main()
