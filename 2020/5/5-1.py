import sys

class BoardingPass(object):
  def __init__(self, spec=None):
    if spec:
      self._s = spec
      self._Populate()

  @property
  def spec(self):
    return self._s

  @spec.setter
  def spec(self, val):
    self._s = spec
    self._Populate()

  @property
  def row(self):
    return self._row

  @property
  def column(self):
    return self._col

  @property
  def id(self):
    return (self._row * 8) + self._col

  def _Reduce(self, spec,  min_val, max_val, lower='F', upper='B'):
    print ('reducing based on %s' % (spec, ))
    for c in spec:
      if c == lower:
        max_val = (max_val + min_val) / 2
        print ('max to %d' % (max_val, ))
      if c == upper:
        min_val = (max_val + min_val) / 2 +1
        print ('min to %d' % (min_val, ))
    if min_val != max_val:
      raise ValueError('unsuccessful reduce: %d != %d' % (min_val, max_val))
    print ('reduced = %d' % (min_val, ))
    return min_val
      
  def _Populate(self):
    self._row = self._Reduce(self._s[0:7], 0, 127)
    self._col = self._Reduce(self._s[7:], 0, 7, lower='L', upper='R')


def main():
  with open('input.txt') as f:
    lines = f.readlines()

  max_id = 0
  for l in lines:
    p = BoardingPass(l.strip('\n'))
    if p.id > max_id:
      max_id = p.id

  print('Highest ID: %d' % (max_id, ))

main()
