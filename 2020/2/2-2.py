import sys

class PasswordFilter(object):
  def __init__(self, f):
    self._IngestFilter(f)

  def _IngestFilter(self, f):
    policy = f.strip()
    (p_pos, p_char) = policy.split(' ')
    (pos1, pos2) = p_pos.split('-')
    self._char = p_char
    self._pos1 = int(pos1)
    self._pos2 = int(pos2)

  @property
  def pos1(self):
    return self._pos1

  @property
  def pos2(self):
    return self._pos2

  @property
  def char(self):
    return self._char


class PasswordSequenceLengthFilter(PasswordFilter):
  def ok(self, p):
    char_count = len([a for a in p if a == self.char])
    if self.pos1 <= char_count <= self.pos2:
      return True
    return False


class PasswordXORFilter(PasswordFilter):
  def ok(self, p):
    if p[self.pos1-1] == self.char and p[self.pos2-1] == self.char:
      return False
    if p[self.pos1-1] != self.char and p[self.pos2-1] != self.char:
      return False
    return True


def main():
  with open(sys.argv[1]) as f:
    lines = f.readlines()

  ok_count = 0

  for line in lines:
      (policy, password) = line.split(':')
      password = password.strip('\n')
      password = password.strip()
      f = PasswordXORFilter(policy)
      if f.ok(password):
        ok_count += 1

  print ('%d OK passwords' % (ok_count, ))
  
main()
