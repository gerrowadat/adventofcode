import sys

def repeats(word):
  reps = {}
  for i in range(0, len(word)-1):
    pair = word[i:i+2]
    pair_count = len([i for i in range(0, len(word) -1) if word[i:i+2] == pair])
    pair_idx = [i for i in range(0, len(word) -1) if word[i:i+2] == pair]
    if pair_count > 1:
      for idx in pair_idx:
        if idx != i and abs(idx - i) != 1 :
          reps[pair] = True
  return reps.keys()

def sandwiches(word):
  sandwiches = {}
  for i in range(0, len(word) - 2):
    if word[i] == word[i+2]:
      sandwiches[i] = True
  return [word[x:x+3] for x in sandwiches.keys()]

def is_nice(word):
  print('%s' % (word, ))
  rep = repeats(word)
  nyom = sandwiches(word)
  if rep:
    print(' - repeats: %s' % (rep, ))
  if nyom:
    print(' - sandwiches: %s' % (nyom, ))

  if not (rep and nyom):
    return False

  return True

if len(sys.argv) > 1:
  print(is_nice(sys.argv[1]))
  sys.exit(0)

nice = 0
with open('input.txt') as f:
  for line in f:
    if is_nice(line.strip('\n')):
      nice += 1

print ('Nice: %d' % (nice, ))

