def neighbours(z,x,y):
  n = [] 
  for z_loc in (z-1, z, z+1):
    for x_loc in (x-1, x, x+1):
      for y_loc in (self.y-1, self.y, self.y+1):
        if not (z == z_loc and x == x_loc and y == y_loc):
          n.append((z,x,y))
  return n


class Grid(object):
  def __init__(self):
    self._p = {}

  def __str__(self):
    ret = ''
    for z in range(min(self._p), max(self._p)+1):
      ret += 'z=%d\n' % (z, )
      for x in range(0, len(self._p[z])):
        for y in range(0, len(self._p[z][x])):
          ret += '#' if self.get(z,x,y) else '.'
        ret += '\n'
    return ret
      
  def get(self, z, x, y):
    if z not in self._p or x not in self._p[z] or y not in self._p[z][x]:
      return False
    return self._p[z][x][y]

  def get_neighbours(self, z, x, y):
    n = [] 
    for z_loc in (z-1, z, z+1):
      for x_loc in (x-1, x, x+1):
        for y_loc in (y-1, y, y+1):
          if not (z == z_loc and x == x_loc and y == y_loc):
            n.append((z_loc,x_loc,y_loc))
    return n

  def get_active(self):
    act = []
    for z in self._p:
      for x in self._p[z]:
        for y in self._p[z][x]:
          if self._p[z][x][y] is True:
            act.append((z,x,y))
    return act
          
  def get_inactive(self):
    return [p for p in self._p if not p.active]

  def set_active(self, z, x, y):
    self.set_point(z,x,y,True)
    
  def set_point(self, z, x, y, val):
    if z not in self._p:
      self._p[z] = {}
    if x not in self._p[z]:
      self._p[z][x] = {}

    self._p[z][x][y] = val
    
  def consider_point(self, z,x,y):
    n_active = []
    p = self.get(z,x,y)
    for n in self.get_neighbours(z,x,y):
      this_p = self.get(n[0], n[1], n[2])
      if this_p:
        n_active.append((n[0], n[1], n[2]))

    if p == True:
      if len(n_active) not in (2,3):
        return False
      return True
    if p == False:
      if len(n_active) == 3:
        return True
      return False

  def backfill(self):
    min_x = min([min(self._p[x]) for x in self._p])
    max_x = max([max(self._p[x]) for x in self._p])
    (min_y, max_y) = (0,0)
    for z in self._p:
      miny = min(self._p[z].keys())
      if miny < min_y:
        min_y = miny
      maxy = max(self._p[z].keys())
      if maxy > max_y:
        max_y = maxy
    for z in self._p:
      for x in range(min_x, max_x+1):
        if x not in self._p[z]:
          self._p[z][x] = {}
          continue
        for y in range(min_y, max_y+1):
          if y not in self._p[z][x]:
            self._p[z][x][y] = False

  def cycle(self):
    set_act = []
    set_inact = []

    to_consider = []

    for z in self._p:
      for x in self._p[z]:
        for y in self._p[z][x]:
          to_consider.append((z,x,y))
          for n in self.get_neighbours(z,x,y):
            to_consider.append((n[0], n[1], n[2]))

    to_consider = set(to_consider)

    for p in to_consider:
      val = self.get(p[0], p[1], p[2])
      new_val = self.consider_point(p[0], p[1], p[2])
      if new_val != val:
        if new_val == True:
          set_act.append((p[0], p[1], p[2]))
        else:
          set_inact.append((p[0], p[1], p[2]))

    for p in set(set_act):
      self.set_point(p[0], p[1], p[2], True)

    for p in set(set_inact):
      self.set_point(p[0], p[1], p[2], False)

    self.backfill()

        
          
def main():
  with open('input.txt') as f:
    raw = f.readlines()

  grid = Grid()
  
  x = 0
  for r in raw:
    chars = [c for c in r.strip('\n')]
    y = 0
    for c in chars:
      grid.set_point(0,x,y, True if c == '#' else False)
      y += 1
    x += 1

  print(grid)

  grid.cycle()
  grid.cycle()
  grid.cycle()
  grid.cycle()
  grid.cycle()
  grid.cycle()

  #print(grid)

  print('Active: %d' % len(grid.get_active()))



main()
