import sys

class Slope(object):
  def __init__(self, slopelines):
    self._s = []

    transposed = []
    for l in slopelines:
      l = l.strip('\n')
      row = [c for c in l]
      transposed.append(row)

    self._s = [list(x) for x in zip(*transposed)]
    # This is apprently how you get python to duplicate a list, wtf.
    self._s_tile = []
    self._s_tile.extend(self._s)

  def __str__(self):
    ret = ''
    for idx in range(0, self.depth):
      ret += ('%s\n' % (''.join([self._s[x][idx] for x in range(0, self.width)])))
    return ret

  @property
  def width(self):
    return len(self._s)

  @property
  def depth(self):
    return len(self._s[0])

  def extend(self):
    self._s.extend(self._s_tile)

  def at(self, x, y):
    if abs(y) > self.depth:
      return None
    print('get %d %d (depth %s)' % (x, y, self.depth))
    if x >= self.width:
      self.extend()
      return self.at(x,y)
    if y >= self.depth:
      return None

    return self._s[x][-y]

  def visit(self, x, y, replace='O'):
    print('visiting %d, %d, with %s' % (x, y, replace))
    self._s[x][-y] = replace
  

class Cursor(object):
  def __init__(self):
    self._x = 0
    self._y = 0

  def __str__(self):
    return '[%d, %d]' % (self._x, self._y)

  @property
  def x(self):
    return self._x

  @x.setter
  def x(self, var):
    self._x = var

  @property
  def y(self):
    return self._y

  @y.setter
  def y(self, var):
    self._y = var


class Descent(object):
  def __init__(self, slope):
    self._s = slope
    self._c = Cursor()
    self._t = 0
    self._consume()

  @property
  def cursor(self):
    return self._c

  @property
  def trees(self):
    return self._t

  @property
  def finished(self):
    if self.cursor.y <= -(self._s.depth-1):
      return True
    return False

  def _consume(self):
    token = self._s.at(self.cursor.x, self.cursor.y)
    if token == '#':
      self._t += 1
      self._s.visit(self.cursor.x, self.cursor.y, replace='X')
    else:
      self._s.visit(self.cursor.x, self.cursor.y, replace='O')
    return token

  def move(self, x_inc, y_inc):
    self.cursor.y += y_inc
    self.cursor.x += x_inc
    self._consume()

  def down(self):
    print('down')
    self.move(0, -1)
 
  def right(self):
    print('right')
    self.move(1, 0)

  def descend(self, x, y):
    print('Cursor before: %s' % (self.cursor, ))
    self.move(x, y)
    print('Cursor after: %s' % (self.cursor, ))

def count_trees_for_path(lines, x, y):
  sl = Slope(lines)
  d = Descent(sl)
  while not d.finished:
    d.descend(x, y)
  return d.trees
  

def main():
  with open(sys.argv[1]) as f:
    lines = f.readlines()

  total_trees = 1

  for path in [(1, -1), (3, -1), (5, -1), (7, -1), (1, -2)]:
    trees = count_trees_for_path(lines, path[0], path[1])
    print('Trees encountered on %s: %d' % (path, trees))
    total_trees = total_trees * trees

  print ('Tree Multiplier: %d' % (total_trees, ))
  
main()
