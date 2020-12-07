import re

def parserule(rule):
  """Return (outer: (inner: inner_count) ...))"""
  rule = rule.strip('.')
  rule = rule.strip(',')
  (outer, inner) = rule.split(' contain ')
  # This is always ' bags'
  outer = outer[0:-5]
  # sigh....fine.
  colourcounts = {}
  for group in re.findall(r'(\d+)\s(.+?\s.+?)\b', inner):
    colourcounts[group[1]] = int(group[0])
  return (outer, colourcounts)

def bag_count(rules, colour):
  if len(rules[colour]) == 0:
    return 1
  count = 1 # This bag itself.
  for bagcolour in rules[colour]:
    count += (rules[colour][bagcolour] * bag_count(rules, bagcolour))
  print('a %s bag is actually %d bags' % (colour, count))
  return count
    
with open("input.txt") as f:
  lines = f.readlines()

rules = dict([parserule(x.strip('\n')) for x in lines])

print('A shiny gold bag (including itself) comprises %d bags' % (bag_count(rules, "shiny gold")))
