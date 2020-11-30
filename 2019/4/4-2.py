#!/usr/bin/python

import sys

def is_ascending(word):
  for idx in range(0, len(word)-1):
    if word[idx] > word[idx+1]:
      return False
  return True

def get_repeats(word):
  repeats = []
  in_repeat = False
  start = None
  end = None
  for idx in range(1, len(word)):
    if word[idx] == word[idx-1]:
      if in_repeat:
        # finish up if this is the last digit
        if idx == (len(word)-1):
          repeats.append(word[start:idx+1])
        continue
      else:
        start = idx-1
        if idx == (len(word)-1):
          repeats.append(word[start:idx+1])
        in_repeat = True
    else:
      if in_repeat:
        end = idx
        repeats.append(word[start:end])
        in_repeat=False
  return repeats

def suitable_password(password):
  if is_ascending(password) and 2 in [len(x) for x in get_repeats(password)]:
    return True
  return False

count = 0

#print('Arg: %s (%s): %s' % (sys.argv[1], get_repeats(sys.argv[1]), suitable_password(sys.argv[1])))

for i in range(254032, 789861):
  if suitable_password(str(i)):
    count += 1

print('Suitable Password in range: %d' % (count, ))
