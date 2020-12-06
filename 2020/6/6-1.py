with open('input.txt') as f:
    raw = f.read()

groups = raw.split('\n\n')

total = 0
for g in groups:
  yes = {}
  for c in g:
    if c.isalpha():
      yes[c] = True
  total += len(yes.keys())

print('Total yes answers: %d' % (total, ))
