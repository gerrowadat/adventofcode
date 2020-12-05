with open('input.txt') as f:
  path = f.readline().strip('\n')

(x, y) = [0, 0]
visits = {}

for c in path:
  visits[(x, y)] = True
  if c == '>':
    x += 1
  elif c == '<':
    x -= 1
  elif c == '^':
    y += 1
  elif c == 'v':
    y -= 1
  visits[(x, y)] = True

print('Houses Visited: %d' % (len(visits.keys())))
