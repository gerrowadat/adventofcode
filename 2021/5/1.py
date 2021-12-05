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
        else:
            return ([Point(n, self.start.y) for n in range(min(self.start.x, self.end.x), max(self.start.x, self.end.x)+1)])

def main():
    with open('input.txt') as f:
        file_lines = [x.strip() for x in f.readlines()]

    lines = []
    
    for l in file_lines:
        # Only consider horizontal/vertical
        line = Line(l)
        if (line.start.x == line.end.x or line.start.y == line.end.y):
            lines.append(line)

    point_counts = {}

    for l in lines:
        for p in l.all_points():
            point_counts[p] = point_counts.get(p, 0) + 1

    intersection_points = len([x for x in point_counts.keys() if point_counts[x] > 1])

    print ('Intersections: %d' % (intersection_points))


if __name__ == '__main__':
    main()
