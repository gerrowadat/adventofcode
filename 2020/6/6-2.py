with open('input.txt') as f:
    raw = f.read()

groups = raw.split('\n\n')

total = 0
for g in groups:
  all_yes = {}
  group_size = len(g.strip('\n').split('\n'))
  for letter in 'abcdefghijklmnopqrstuvwxyz':
    yes_count = len([x for x in g if x == letter])
    if yes_count == group_size:
      all_yes[letter] = True
  total += len(all_yes.keys())

print('Total unanimous yes answers: %d' % (total, ))
