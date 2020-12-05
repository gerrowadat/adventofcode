with open('input.txt') as f:
  line = f.readline().strip('\n')
  pos = 0
  idx = 1
  for c in line:
    if c == '(':
      pos += 1
    if c == ')':
      pos -= 1
    if pos < 0:
      print ('Entered Basement at position %d' % (idx, ))
      break
    idx += 1
