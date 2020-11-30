#!/usr/bin/python


def try_nounverb(p, noun, verb):
  p[1] = noun
  p[2] = verb

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
      print('halt (result: %d)' % (p[0], ))
      return p[0]
    c += 4

def get_program():
  with open('input.txt') as f:
    p_line = f.readline()

  return [int(x) for x in p_line.split(',')]


for noun in range(0,100):
  for verb in range(0,100):
    result = try_nounverb(get_program(), noun, verb)
    print('Noun: %d Verb: %d Result: %d' % (noun, verb, result))
    if result == 19690720:
      print('RESULT: Noun: %d Verb: %d' % (noun, verb))
      break

print('Not Found')
