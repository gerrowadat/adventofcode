import time

def bus_is_at(b, ts):
  #print ('@%d: %d mod %d == %d?' % (ts, ts, b, offset))
  return ts % b == 0

def buses_at(buses, ts):
  if ts < len(buses):
    if buses[ts] == 'x':
      return []
    return buses[ts]

  ret = []
  for i in range(0, len(buses)):
    if buses[i] == 'x':
      continue
    if bus_is_at(int(buses[i]), ts):
      ret.append(int(buses[i]))
  return ret

def is_seq_at(buses, ts):

  for i in range(0, len(buses)):
    b = buses_at(buses, ts + i)
    if buses[i] == 'x':
      if len(b) != 0:
        return False
    if len(b) == 0:
      if buses[i] != 'x':
        return False
    if len(b) == 1:
      if b[0] != int(buses[i]):
        #print ('len 1 %d not %d' % (b[0], int(buses[i])))
        return False
    if len(b) > 1:
      if i != len(buses)-1:
        #print('more then 1 but not last')
        return False
      if buses[i] not in b:
        return False
  return True


def printsched(buses, start, offset):
  print ('time\t%s' % ('\t'.join([x for x in buses if x != 'x']), ))
  for i in range(0, offset):
    at = buses_at(buses, start + i)
    print('%d\t%s' % ((start+i), '\t'.join(['D' if int(x) in at else '.' for x in buses if x != 'x'])))
    

def main():
  with open('input.txt') as f:
    f.readline()
    buses = f.readline().strip('\n').split(',')
    #buses = '17,x,13,19'.split(',')
    #buses = '67,7,59,61'.split(',')
    #buses = '1789,37,47,1889'.split(',')

  #printsched(buses, 3417, 20)
  #print('%s' % (is_seq_at(buses, 3417)))

  #return
  tick = 0
  # omg a clue
  count = 100000000000000 / int(buses[0])
  while True:
    count += 1
    ts = int(buses[0]) * count
    if time.time() > tick + 1:
      print ('Checking %d' % (ts,))
      tick = time.time()
    if is_seq_at(buses, ts):
      printsched(buses, ts, 30)
      print('Found sequence at %d' % (ts, ))
      return

      
main()
