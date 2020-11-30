#!/usr/bin/python


def is_ascending(num_str):
  for idx in range(0, len(num_str)-1):
    if num_str[idx] > num_str[idx+1]:
      return False
  return True

def has_double(num_str):
  for idx in range(0, len(num_str)-1):
    if num_str[idx] == num_str[idx+1]:
      return True
  return False

def suitable_password(password):
  if is_ascending(password) and has_double(password):
    return True
  return False

count = 0

for i in range(254032, 789861):
  if suitable_password(str(i)):
    count += 1
  

print('Suitable Password in range: %d' % (count, ))
