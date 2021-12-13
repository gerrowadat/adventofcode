#!/usr/bin/env python3

class Dot(object):
    def __init__(self, x, y):
        self._x = int(x)
        self._y = int(y)

    def __str__(self):
        return '(%d, %d)' % (self._x, self._y)

    def __eq__(self, other):
        if self.x == other.x and self.y == other.y:
            return True
        return False

    def __hash__(self):
        return hash('%d,%d' % (self._x, self._y))

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, val):
        self._x = int(val)

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, val):
        self._y = int(val)



class Paper(object):
    def __init__(self):
        self._g = []

    def __str__(self):
        ret = ''
        for i in range(self.y_len+1):
            for j in range(self.x_len+1):
                if self.is_dot(j, i):
                    ret += '#'
                else:
                    ret += '.'
            ret += '\n'
        return ret

    @property
    def x_len(self):
        return max([dot.x for dot in self._g])

    @property
    def y_len(self):
        return max([dot.y for dot in self._g])

    def is_dot(self, x, y):
        if len([d for d in self._g if d.x == x and d.y == y]) > 0:
            return True
        return False

    def visible_dots(self):
        return len(set(self._g))

    def add_dot(self, x, y):
        self._g.append(Dot(x, y))

    def fold(self, axis, pos):
        if axis == 'y':
            # fold up along axis at y=
            for d in self._g:
                if d.y > pos:
                    new_y = d.y - ((d.y - pos) * 2)
                    d.y = new_y

        if axis == 'x':
            # fold left along axis at x=
            for d in self._g:
                if d.x > pos:
                    new_x = d.x - ((d.x - pos) * 2)
                    d.x = new_x


def main():
    with open('input.txt') as f:
        lines = [x.strip() for x in f.readlines()]

    p = Paper()
    folds = []

    for l in [x for x in lines if x != ""]:
        if l.startswith('fold'):
            (axis, pos) = l.split()[2].split('=')
            folds.append((axis, int(pos)))
        else:
            (x, y) = l.split(',')
            p.add_dot(x, y)

    for f in folds:
        p.fold(*f)

    print(p)

if __name__ == '__main__':
    main()
