def adjacent_occupied_seats(plan, i, j):
  seats = []
  for idx in (i-1, i, i+1):
    seats.extend([(idx, j-1), (idx, j), (idx, j+1)])

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
        if adj >= 4:
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
