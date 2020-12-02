import sys

class PasswordFilter(object):
  def __init__(self, char, min_count, max_count):
    self._char = char
    self._min_count = int(min_count)
    self._max_count = int(max_count)

  def ok(self, password):
    char_count = len([a for a in password if a == self._char])
    if self._min_count <= char_count <= self._max_count:
      return True
    return False

def main():
  with open(sys.argv[1]) as f:
    lines = f.readlines()

  ok_count = 0

  for line in lines:
      (policy, password) = line.split(':')
      password = password.strip('\n')
      password = password.strip()
      policy = policy.strip()
      (p_range, p_char) = policy.split(' ')
      (pr_min, pr_max) = p_range.split('-')
      print('Filtering for %s to %s of %s in %s' % (pr_min, pr_max, p_char, password))
      f = PasswordFilter(p_char, pr_min, pr_max)
      if f.ok(password):
        ok_count += 1

  print ('%d OK passwords' % (ok_count, ))
  
main()
