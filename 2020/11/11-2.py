def look(plan, i, j, i_step, j_step):
  here_i = i
  here_j = j
  while (0 <= here_i < len(plan)) and (0 <= here_j < len(plan[0])):
    if plan[here_i][here_j] in ('L', '#'):
      if not (here_i == i and here_j == j):
        return [here_i, here_j]
    here_i += i_step
    here_j += j_step
  return []

def seen_seats(plan, i, j):
  all_seen = []

  for x in (-1, 0, 1):
    for y in (-1, 0, 1):
      if x == 0 and y == 0:
        continue
      seen = look(plan, i, j, x, y)
      if seen:
        all_seen.append(seen)

  return all_seen

def get_changes(plan):
  changes = []

  for i in range(0, len(plan)):
    for j in range(0, len(plan[i])):
      if plan[i][j] in ('L', '#'):
        occupied = len([x for x in seen_seats(plan, i, j) if plan[x[0]][x[1]] == '#'])
        if plan[i][j] == 'L':
          if occupied == 0:
            changes.append((i, j, '#',))
        if plan[i][j] == '#':
          if occupied >= 5:
            changes.append((i, j, 'L',))

  return changes

def main():
  with open('input.txt') as f:
    rows = [x.strip('\n') for x in f.readlines()]
  plan = [list(x) for x in rows]

  while True:
    changes = get_changes(plan)
    if not changes:
      break
    for c in changes:
      plan[c[0]][c[1]] = c[2]

  occupied = sum([len([y for y in plan[x] if y == '#']) for x in range(0, len(plan))])

  print('%s' % '\n'.join([''.join(x) for x in plan]))

  print('Occupied seats: %d' % (occupied, ))


main()
