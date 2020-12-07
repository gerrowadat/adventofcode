import re
import sys

def parserule(rule):
  rule = rule.strip('.')
  rule = rule.strip(',')
  (outer, inner) = rule.split(' contain ')
  outer = outer[0:-5]
  # sigh....fine.
  m = re.findall(r'\d+\s(.+?\s.+?)\b', inner)
  return (outer, m)

def contained_by(rules, colour):
  directs = set([i for i in rules if colour in rules[i]])
  indirects = []
  for d in directs:
    indirects.extend(contained_by(rules, d))
  directs.update(indirects)
  return directs

if len(sys.argv) > 1:
  print parserule(sys.argv[1])

with open("input.txt") as f:
  lines = f.readlines()

rules = dict([parserule(x.strip('\n')) for x in lines])

valid = contained_by(rules, "shiny gold")

print('Valid outer bags: %d' % (len(valid)))
