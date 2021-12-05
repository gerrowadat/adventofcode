#!/usr/bin/env python3

class Point(object):
    def __init__(self, x, y):
        self._x = x
        self._y = y

    def __str__(self):
        return '(%s,%s)' % (self.x, self.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash(str(self))

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y


class Line(object):
    def __init__(self, spec):
        # x1,y1 -> x2,y2
        coords = spec.split(' -> ')
        if len(coords) != 2:
            raise ValueError('funny looking spec %s' % (spec, ))
        (self._x1, self._y1) = [int(x) for x in coords[0].split(',')]
        (self._x2, self._y2) = [int(x) for x in coords[1].split(',')]

    def __str__(self):
        return '%s,%s --> %s,%s' % (self._x1, self._y1, self._x2, self._y2)

    @property
    def start(self):
        return Point(self._x1, self._y1)

    @property
    def end(self):
        return Point(self._x2, self._y2)

    def all_points(self):
        if self.start.x == self.end.x:
            return ([Point(self.start.x, n) for n in range(min(self.start.y, self.end.y), max(self.start.y, self.end.y)+1)])
        elif self.start.y == self.end.y:
            return ([Point(n, self.start.y) for n in range(min(self.start.x, self.end.x), max(self.start.x, self.end.x)+1)])
        else:
            if self.start.x < self.end.x:
                x_range = list(range(self.start.x, self.end.x+1))
            else:
                x_range = list(range(self.start.x, self.end.x-1, -1))
            if self.start.y < self.end.y:
                y_range = list(range(self.start.y, self.end.y+1))
            else:
                y_range = list(range(self.start.y, self.end.y-1, -1))
            ret = []
            for i in range(len(x_range)):
                ret.append(Point(x_range[i], y_range[i]))
            return ret


def main():
    with open('input.txt') as f:
        file_lines = [x.strip() for x in f.readlines()]

    lines = []
    
    for l in file_lines:
        lines.append(Line(l))

    point_counts = {}

    for l in lines:
        for p in l.all_points():
            point_counts[p] = point_counts.get(p, 0) + 1

    intersection_points = len([x for x in point_counts.keys() if point_counts[x] > 1])

    print ('Intersections: %d' % (intersection_points))


if __name__ == '__main__':
    main()
