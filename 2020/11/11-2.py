def diag(plan, i, j, i_step, j_step, verbose=False):
  here_i = i
  here_j = j
  while (0 <= here_i < len(plan)) and (0 <= here_j < len(plan[0])):
    if verbose:
      print(' - %d,%d: %s' % (here_i, here_j, plan[here_i][here_j]))
    if plan[here_i][here_j] in ('L', '#'):
      if not (here_i == i and here_j == j):
        return [here_i, here_j]
    here_i += i_step
    here_j += j_step
    if verbose:
      print('%d,%d considering %d,%d' % (i, j, here_i, here_j))
  return []

def seen_seats(plan, i, j):
  seen = []

  w = diag(plan, i, j, 0, -1)
  if w:
    seen.append(w)

  e = diag(plan, i, j, 0, 1)
  if e:
    seen.append(e)

  n = diag(plan, i, j, -1, 0)
  if n:
    seen.append(n)

  s = diag(plan, i, j, 1, 0)
  if s:
    seen.append(s)

  ne = diag(plan, i, j, 1, 1)
  if ne:
    seen.append(ne)

  nw = diag(plan, i, j, -1, 1)
  if nw:
    seen.append(nw)

  se = diag(plan, i, j, 1, -1)
  if se:
    seen.append(se)

  sw = diag(plan, i, j, -1, -1)
  if sw:
    seen.append(sw)

  return seen

def adjacent_occupied_seats(plan, i, j):
  seats = seen_seats(plan, i, j)

  adj = []
  for s in seats:
    if s != (i, j):
      if s[0] >= 0 and s[1] >= 0:
        if s[0] < len(plan) and s[1] < len(plan[0]):
          adj.append(s)
  occ = []
  for s in adj:
      if plan[s[0]][s[1]] == '#':
        occ.append(s)
  return occ

def get_changes(plan):
  changes = []
  for i in range(0, len(plan)):
    for j in range(0, len(plan[i])):
      if plan[i][j] == 'L':
        adj = len(adjacent_occupied_seats(plan, i, j))
        if adj == 0:
          changes.append((i, j, '#',))
      if plan[i][j] == '#':
        adj = len(adjacent_occupied_seats(plan, i, j))
        if adj >= 5:
          changes.append((i, j, 'L',))
  return changes

def printplan(plan):
    for row in plan:
      print ''.join(row)

def main():
  with open('input.txt') as f:
    rows = [x.strip('\n') for x in f.readlines()]
  plan = [list(x) for x in rows]

  done = False

  while not done:
    changes = get_changes(plan)
    if not changes:
      break
    for c in changes:
      plan[c[0]][c[1]] = c[2]

  occupied = 0
  for row in plan:
    occupied += len([x for x in row if x == '#'])

  printplan(plan)

  print('Occupied seats: %d' % (occupied, ))


main()
