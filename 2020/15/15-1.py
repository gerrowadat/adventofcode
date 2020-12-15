def main():
  #start = [1, 3, 2]
  #start = [3,1,2]
  start = [7,12,1,0,16,2]

  turns = {}

  turnc = -1 

  for s in start:
    turnc += 1
    turns[turnc] = s

  while turnc != 2020:
    turnc += 1
    prev = [x for x in turns if turns[x] == turns[turnc-1]]

    if len(prev) == 1:
      turns[turnc] = 0 
      continue

    turns[turnc] = prev[-1] - prev[-2]

  print ('turns: %s' % (turns[turnc-1]))
      



main()
