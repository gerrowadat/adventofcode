
def is_nice(word):
  # if not enough vowels..
  if len([c for c in word if c in 'aeiou']) < 3:
    return False
  # If not doubles...
  if len([i for i in range(1, len(word)) if word[i-1] == word[i]]) == 0:
    return False
  for bad in ['ab', 'cd', 'pq', 'xy']:
    if bad in word:
      return False
  return True

nice = 0
with open('input.txt') as f:
  for line in f:
    if is_nice(line.strip('\n')):
      nice += 1

print ('Nice: %d' % (nice, ))

