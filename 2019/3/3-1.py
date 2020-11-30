#!/usr/bin/python

import sys


class Point(object):
  def __init__(self, x, y):
    self._x = x
    self._y = y

  def __str__(self):
    return '[%d,%d]' % (self.x, self.y)

  def __eq__(self, other):
    if self.x == other.x and self.y == other.y:
      return True
    return False

  @property
  def distance(self):
    return abs(self.x) + abs(self.y)
  
  @property
  def x(self):
    return self._x

  @property
  def y(self):
    return self._y

class Line(object):
  def __init__(self, start, vector):
    """start (Point): the start of the line
       vector (str): The UDLR vector of the line i.e. U8, D500"""
    self._start = start
    self._vector = vector
    self._direction = vector[0]
    self._length = int(vector[1:])
    self._end = self._GetEnd()

  def __str__(self):
    return '%s -> %s' % (str(self._start), str(self._end))

  def _GetEnd(self):
    if self.direction not in ('U', 'D', 'L', 'R'):
      raise ValueError('%s not in UDLR formet' % (self._vector, ))
    if self.direction == 'U':
      return Point(self.start.x, self.start.y + self.length)
    elif self.direction == 'D':
      return Point(self.start.x, self.start.y - self.length)
    elif self.direction == 'R':
      return Point(self.start.x + self.length, self.start.y)
    elif self.direction == 'L':
      return Point(self.start.x - self.length, self.start.y)

  def _GetPoints(self):
    """Given the origin point tuple and a UDLR direction, return an ordered list of tuples alng that line."""
    points = []

    if self.direction not in ('U', 'D', 'L', 'R'):
      raise ValueError('%s not in UDLR formet' % (self._vector, ))
    if self.direction == 'U':
      for y in range(self.start.y, self.start.y + self.length + 1):
        points.append(Point(self.start.x, y))
    elif self.direction == 'D':
      for y in range(self.start.y, self.start.y - self.length - 1, -1):
        points.append(Point(self.start.x, y))
    elif self.direction == 'R':
      for x in range(self.start.x, self.start.x + self.length + 1):
        points.append(Point(x, self.start.y))
    elif self.direction == 'L':
      for x in range(self.start.x, self.start.x - self.length -1, -1):
        points.append(Point(x, self.start.y))

    return points
     
  @property
  def points(self):
    return self._GetPoints()

  @property
  def start(self):
    return self._start

  @property
  def end(self):
    return self._end

  @property
  def direction(self):
    return self._direction

  @property
  def length(self):
    return self._length


def get_lines(vectors):
  """Given a set uf UDLR directions, return a list of lines."""
  start_point = Point(0,0)
  lines = []
  for vec in vectors:
    line = Line(start_point, vec)
    lines.append(line)
    start_point = line.end
  return lines

def is_between(a, b, val):
  if a < b:
    return a <= val <= b
  return b <= val <= a

def get_intersection(a, b):
  # This assumes intersections are perpendicular (i.e. wires never meet end-on).
  if a.direction in ['U', 'D'] and  b.direction in ['U', 'D']:
    return None
  if a.direction in ['L', 'R'] and  b.direction in ['L', 'R']:
    return None

  # The other line is perpendicular. Knowing our line's orientation helps.
  if a.direction in ('U', 'D'):
    for p in a.points:
      if b.start.y == p.y and is_between(b.start.x, b.end.x, p.x):
        return p

  if a.direction in ('L', 'R'):
    for p in a.points:
      if b.start.x == p.x and is_between(b.start.y, b.end.y, p.y):
        return p

  return None


def get_intersections(wire1, wire2):
  intersections = []
  for line1 in wire1:
    for line2 in wire2:
      intersection = get_intersection(line1,line2)
      if intersection and intersection.x != 0 and intersection.y != 0:
        print('%s and %s intersect at %s' % (line1, line2, intersection))
        intersections.append(intersection)
  return intersections

with open(sys.argv[1]) as f:
  wire1 = f.readline().strip('\n')
  wire2 = f.readline().strip('\n')

wire1_lines = get_lines(wire1.split(','))
wire2_lines = get_lines(wire2.split(','))

print('Wire1: %d lines' % (len(wire1_lines)))
print('Wire2: %d lines' % (len(wire2_lines)))

intersections = get_intersections(wire1_lines, wire2_lines)

print('Intersections [%d]: %s' % (len(intersections), [str(x) for x in intersections]))

distances = {}
for point in intersections:
  distances[point.distance] = point

closest = sorted(distances.keys())[0]

print('Closest intersection: %s (%d)' % (distances[closest], distances[closest].distance))
