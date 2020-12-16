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

  @property
  def name(self):
    return self._name

  def num_valid(self, num):
    for r in self._ranges:
      if r[0] <= num <= r[1]:
        return True

    return False


class Ticket(object):
  def __init__(self, numstr, rules):
    self._nums = [int(x) for x in numstr.split(',')]
    self._r = rules
    
  @property
  def nums(self):
    return self._nums

  @property
  def rules(self):
    return self._r

  @property
  def valid(self):
    if len(self.invalid_nums()) == 0:
      return True
    return False

  def valid_fields(self, idx):
    valid = []
    for r in self._r:
      if r.num_valid(self._nums[idx]):
        valid.append(r.name)
    return valid


  def invalid_nums(self):
    inv = []
    for n in self._nums:
      passes = [p for p in [x.num_valid(n) for x in self._r] if p is True]
      if not passes:
        inv.append(n)
    return inv

def main():
  l = None
  rule_lines = []
  with open('input.txt') as f:
    while True:
      l = f.readline()
      if l == '\n':
        break
      rule_lines.append(l.strip('\n'))
    # my ticket preamble
    f.readline()
    my_tick = f.readline().strip('\n')
    # newline
    f.readline()
    # nearby ticket preamble
    f.readline()
    nearby = f.readlines()

  rules = [TicketRule(x) for x in rule_lines]

  my_tick = Ticket(my_tick, rules)
  all_ticks = [Ticket(t, rules) for t in nearby]
  ticks = [x for x in all_ticks if x.valid]

  known = {}

  # Go through the list of rules repeatedly, narrowing down the 
  # possible columns only when we have a clear winner.
  while len(known) < len(ticks[0].nums):
    for r in [x for x in rules if x.name not in known.keys()]:
      valids = {}
      for col in [x for x in range(0, len(ticks[0].nums)) if x not in known.values()]:
        colnums = [x.nums[col] for x in ticks]
        valids[col] = len([x for x in colnums if r.num_valid(x)])
      # Remove if there is a clear winner.
      max_valid = max(valids, key=valids.get)
      if len([x for x in valids if valids[x] == valids[max_valid]]) == 1:
        known[r.name] = max_valid
        print ('%s is %d' % (r.name, max_valid))

  print('\n')

  result = 1
  for fname in [x for x in known if x.startswith('departure')]:
    print('%s: %d' % (fname, my_tick.nums[known[fname]]))
    result = result * my_tick.nums[known[fname]]
  
  print ('Result: %d' % (result, ))
  

main()
