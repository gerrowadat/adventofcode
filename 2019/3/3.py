#!/usr/bin/python

with open('input.txt') as f:
  p_line = f.readline()

p = [int(x) for x in p_line.split(',')]

p[1] = 12
p[2] = 2

c = 0

while True:
  cmd = p[c:c+4]
  if cmd[0] == 1:
    result = p[cmd[1]] + p[cmd[2]]
    p[cmd[3]] = result
    print('%d + %d = %d [stored at %d]' % (p[cmd[1]], p[cmd[2]], result, cmd[3]))
  if cmd[0] == 2:
    result = p[cmd[1]] * p[cmd[2]]
    p[cmd[3]] = result
    print('%d * %d = %d [stored at %d]' % (p[cmd[1]], p[cmd[2]], result, cmd[3]))
  if cmd[0] == 99:
    print 'halt'
    break
  c += 4

print ','.join([str(x) for x in p])
