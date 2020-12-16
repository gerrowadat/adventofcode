class TicketRule(object):
  def __init__(self, rulestr):
    self._raw = rulestr
    self._name = None
    self._ranges = []

    r = self._raw.strip('\n')
    (fieldname, numstr) = r.split(':')
    self._name = fieldname
    for rng in numstr.split(' or '):
      self._ranges.append([int(x) for x in rng.split('-')])

  def num_valid(self, num):
    for r in self._ranges:
      if r[0] <= num <= r[1]:
        return True

    return False


class Ticket(object):
  def __init__(self, numstr, rules):
    self._nums = [int(x) for x in numstr.split(',')]
    self._r = [TicketRule(x) for x in rules]
    
  @property
  def rules(self):
    return self._r

  def invalid_nums(self):
    inv = []
    for n in self._nums:
      passes = [p for p in [x.num_valid(n) for x in self._r] if p is True]
      if not passes:
        inv.append(n)
    return inv

def main():
  l = None
  rules = []
  with open('input.txt') as f:
    while True:
      l = f.readline()
      if l == '\n':
        break
      rules.append(l.strip('\n'))
    # my ticket preamble
    f.readline()
    my_tick = f.readline().strip('\n')
    # newline
    f.readline()
    # nearby ticket preamble
    f.readline()
    nearby = f.readlines()

  rate = 0
  for t in nearby:
    tick = Ticket(t, rules)
    print ('bad: %s' % (tick.invalid_nums()))
    rate += sum(tick.invalid_nums())

  print('Error Rate: %s' % (rate, ))


main()
