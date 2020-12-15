def main():
  #turns = [1, 3, 2]
  #turns = [3,1,2]
  turns = [7,12,1,0,16,2]

  last = {}
  count = 0

  for s in turns:

    last[s] = [count]
    count += 1

  while count != 30000000:
    newnum = None

    if turns[-1] not in last or len(last[turns[-1]]) == 1:
      if 0 in last:
        last[0].append(count)
      else:
        last[0] = [count]
      turns.append(0)
    else:
      newnum = last[turns[-1]][-1] - last[turns[-1]][-2]
      turns.append(newnum)
      if newnum in last:
        last[newnum].append(count)
      else:
        last[newnum] = [count]

    count += 1

  print ('turns: %s' % (turns[-1]))
      



main()
