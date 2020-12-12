class Ship(object):
  def __init__(self):
    self._heading = 90
    self._pos = [0, 0]

  HEADINGS = {
    0 : 'N',
    90 : 'E',
    180 : 'S',
    270 : 'W'
  }

  def __str__(self):
    return('Position %s heading %d' % (str(self.pos), self.heading))

  @property
  def heading(self):
    return self._heading

  @heading.setter
  def heading(self, val):
    self._heading = val

  @property
  def pos(self):
    return self._pos

  def turn(self, direction, degrees):
    if direction == 'R':
      self.heading = (self.heading + degrees) % 360
    if direction == 'L':
      self.heading = (360 + (self.heading - degrees)) % 360

  def forward(self, distance):
    self.go(self.HEADINGS[self.heading], distance)

  def go(self, direction, distance):
    if direction == 'N':
      self._pos[1] += distance
    if direction == 'S':
      self._pos[1] -= distance
    if direction == 'E':
      self._pos[0] += distance
    if direction == 'W':
      self._pos[0] -= distance
    if direction == 'F':
      self.forward(distance)

def main():
  with open('input.txt') as f:
    raw = f.readlines()

  ship = Ship()

  print(ship)

  for line in raw:
    line = line.strip('\n')
    cmd = line[0]
    arg = int(line[1:])
    if cmd in ('L', 'R'):
      ship.turn(cmd, arg)
    else:
      ship.go(cmd, arg)

  print(ship)

  print('Distance: %d' % (abs(ship.pos[0]) + abs(ship.pos[1])))

main()

