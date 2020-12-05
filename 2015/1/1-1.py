with open('input.txt') as f:
  line = f.readline().strip('\n')
  pos = 0
  for c in line:
    if c == '(':
      pos += 1
    if c == ')':
      pos -= 1

print ('Floor: %d' % (pos, ))
