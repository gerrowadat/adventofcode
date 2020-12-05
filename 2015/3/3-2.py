def move(x, y, c):
  if c == '>':
    x += 1
  elif c == '<':
    x -= 1
  elif c == '^':
    y += 1
  elif c == 'v':
    y -= 1
  return (x, y)

with open('input.txt') as f:
  path = f.readline().strip('\n')

(s_x, s_y) = [0, 0]
(r_x, r_y) = [0, 0]
santa = True

visits = {}


for c in path:
  if santa:
    visits[(s_x, s_y)] = True
    (s_x, s_y) = move(s_x, s_y, c)
    visits[(s_x, s_y)] = True
    santa = False
  else:
    visits[(r_x, r_y)] = True
    (r_x, r_y) = move(r_x, r_y, c)
    visits[(r_x, r_y)] = True
    santa = True

print('Houses Visited: %d' % (len(visits.keys())))
