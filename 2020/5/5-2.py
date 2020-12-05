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
    for c in spec:
      if c == lower:
        max_val = (max_val + min_val) / 2
      if c == upper:
        min_val = (max_val + min_val) / 2 +1
    if min_val != max_val:
      raise ValueError('unsuccessful reduce: %d != %d' % (min_val, max_val))
    return min_val
      
  def _Populate(self):
    self._row = self._Reduce(self._s[0:7], 0, 127)
    self._col = self._Reduce(self._s[7:], 0, 7, lower='L', upper='R')


def main():
  with open('input.txt') as f:
    lines = f.readlines()

  ids = {}
  for l in lines:
    p = BoardingPass(l.strip('\n'))
    ids[p.id] = p

  for i in sorted(ids.keys()):
    if (i + 1) not in ids.keys() and (i + 2) in ids.keys():
      print('ID %d is missing and must be yours' % (i + 1))
      col = (i+1) % 8
      row = ((i+1) - col) / 8
      print('Please sit in row %d, column %d' % (row, col))


main()
