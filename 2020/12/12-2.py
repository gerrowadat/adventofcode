class Point(object):
  def __init__(self):
    self._pos = [0, 0]

  def __str__(self):
    return str(self.pos)

  @property
  def pos(self):
    return self._pos

  @pos.setter
  def pos(self, val):
    self._pos = val

  def go(self, direction, distance):
    if direction == 'N':
      self._pos[1] += distance
    if direction == 'S':
      self._pos[1] -= distance
    if direction == 'E':
      self._pos[0] += distance
    if direction == 'W':
      self._pos[0] -= distance

  def rotate(self, origin, direction, degrees):
    if direction == 'R':
      return self.rotate(origin, 'L', 360 - degrees)
 
    #print('rotating %s %d deg around %s' % (str(self.pos), degrees, origin))

    if degrees == 90:
      # (x,y) -> (-y, x)
      new_x = (-(self.pos[1] - origin[1]) + origin[0])
      new_y = ((self.pos[0] - origin[0]) + origin[1])
      self.pos = [new_x, new_y]
      return self.pos

    if degrees == 180:
      # (x,y) -> (-x, -y)
      new_x = (-(self.pos[0] - origin[0]) + origin[0])
      new_y = (-(self.pos[1] - origin[1]) + origin[1])
      self.pos = [new_x, new_y]
      return self.pos

    if degrees == 270:
      # (x,y) -> (y, -x)
      new_x = ((self.pos[1] - origin[1]) + origin[0])
      new_y = (-(self.pos[0] - origin[0]) + origin[1])
      self.pos = [new_x, new_y]
      return self.pos

class Waypoint(Point):
  pass

class Ship(Point):
  def __init__(self):
    super().__init__()
    self._wp = Point()

  def __str__(self):
    return 'pos %s wp %s' % (str(self.pos), str(self.wp))

  @property
  def wp(self):
    return self._wp

  def forward(self):
    diff = ((abs(self.pos[0] - self.wp.pos[0])), (abs(self.pos[1] - self.wp.pos[1])))
    for pos in (0, 1):
      if self.pos[pos] < self.wp.pos[pos]:
        self.pos[pos] += diff[pos]
        self.wp.pos[pos] += diff[pos]
      else:
        self.pos[pos] -= diff[pos]
        self.wp.pos[pos] -= diff[pos]

  def go(self, direction, distance):
    print('%s -> %d' % (direction, distance))
    if direction in ('N', 'E', 'W' ,'S'):
      self.wp.go(direction, distance)
    elif direction in ('L', 'R'):
      self.wp.rotate(self.pos, direction, distance)
    else:
      # F
      for i in range(0, distance):
        self.forward()

def main():
  with open('input.txt') as f:
    raw = f.readlines()

  ship = Ship()
  ship.wp.pos = [10,1]

  print(ship)

  for line in raw:
    line = line.strip('\n')
    cmd = line[0]
    arg = int(line[1:])
    ship.go(cmd, arg)
    print(ship)

  print(ship)

  print('Distance: %d' % (abs(ship.pos[0]) + abs(ship.pos[1])))

main()
