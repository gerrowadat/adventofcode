class Grid(object):
  def __init__(self):
    self._p = {}

  def get(self, z, x, y, w):
    if (z, w) not in self._p or x not in self._p[(z, w)] or y not in self._p[(z, w)][x]:
      return False
    return self._p[(z, w)][x][y]

  def get_neighbours(self, z, x, y, w):
    n = [] 
    for w_loc in (w-1, w, w+1):
      for z_loc in (z-1, z, z+1):
        for x_loc in (x-1, x, x+1):
          for y_loc in (y-1, y, y+1):
            if not (z == z_loc and x == x_loc and y == y_loc and w == w_loc):
              n.append(((z_loc, w_loc), x_loc, y_loc))
    return n

  def get_active(self):
    act = []
    for zw in self._p:
      for x in self._p[zw]:
        for y in self._p[zw][x]:
          if self._p[zw][x][y] is True:
            act.append((zw,x,y))
    return act
          
  def set_point(self, z, x, y, w, val):
    if (z, w) not in self._p:
      self._p[(z, w)] = {}
    if x not in self._p[(z, w)]:
      self._p[(z, w)][x] = {}

    self._p[(z, w)][x][y] = val
    
  def consider_point(self, z,x,y, w):
    n_active = []
    p = self.get(z, x, y, w)
    for n in self.get_neighbours(z,x,y,w):
      this_p = self.get(n[0][0], n[1], n[2], n[0][1])
      if this_p:
        n_active.append((n[0][0], n[1], n[2], n[0][1]))

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
    for zw in self._p:
      miny = min(self._p[zw].keys())
      if miny < min_y:
        min_y = miny
      maxy = max(self._p[zw].keys())
      if maxy > max_y:
        max_y = maxy
    for zw in self._p:
      for x in range(min_x, max_x+1):
        if x not in self._p[zw]:
          self._p[zw][x] = {}
          continue
        for y in range(min_y, max_y+1):
          if y not in self._p[zw][x]:
            self._p[zw][x][y] = False

  def cycle(self):
    set_act = []
    set_inact = []

    to_consider = []

    for zw in self._p:
      for x in self._p[zw]:
        for y in self._p[zw][x]:
          to_consider.append((zw,x,y))
          for n in self.get_neighbours(zw[0],x,y,zw[1]):
            to_consider.append((n[0], n[1], n[2]))

    to_consider = set(to_consider)

    for p in to_consider:
      val = self.get(p[0][0], p[1], p[2], p[0][1])
      new_val = self.consider_point(p[0][0], p[1], p[2], p[0][1])
      if new_val != val:
        if new_val == True:
          set_act.append((p[0], p[1], p[2]))
        else:
          set_inact.append((p[0], p[1], p[2]))

    for p in set(set_act):
      self.set_point(p[0][0], p[1], p[2], p[0][1], True)

    for p in set(set_inact):
      self.set_point(p[0][0], p[1], p[2], p[0][1], False)

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
      grid.set_point(0,x,y,0, True if c == '#' else False)
      y += 1
    x += 1

  for i in range(6):
    grid.cycle()
    print('Active after %d: %d' % (i+1, len(grid.get_active())))


main()
