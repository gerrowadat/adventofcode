def to_36(dec):
  # ell oh ell
  return '{:#038b}'.format(dec)[2:]

def to_dec(bits):
  return int(bits, 2)

def apply_mask(dec, mask):
  dec36 = list(to_36(dec))
  mask = list(mask)
  print('value:\t%s\t(decimal %d)' % (''.join(dec36), dec))
  print('mask:\t%s' % (''.join(mask)))
  for i in range(0, len(dec36)):
    if mask[i] in ('0', '1'):
      dec36[i] = mask[i]
  print('result:\t%s' % (''.join(dec36)))
  return to_dec(''.join(dec36))

def expand_floating(addr):
  if 'X' not in addr:
    return [to_dec(addr)]
  addr = list(addr)
  addrs = []
  x_count = len([x for x in addr if x == 'X'])
  for i in range(0, 2 ** x_count):
    this_addr = list(addr)
    subst = format(i, '0%sb' % (x_count, ))
    s_count = 0
    for i in range(0, len(this_addr)):
      if this_addr[i] == 'X':
        this_addr[i] = subst[s_count]
        s_count += 1
    addrs.append(to_dec(''.join(this_addr)))
  return addrs
        
def get_mem_updates(addr, mask):
  dec36 = list(to_36(addr))
  mask = list(mask)

  # resolve all flips to 1 first...
  for i in range(0, len(dec36)):
    if mask[i] in ('1', 'X'):
      dec36[i] = mask[i]

  return expand_floating(''.join(dec36))

def main():
  with open('input.txt') as f:
    raw = f.readlines()

  mem = {}
  mask = ''
  for line in raw:
    line = line.strip('\n')
    (instr, value) = line.split(' = ')

    if instr == 'mask':
      mask = value
      print('mask is now %s' % (mask, ))

    if instr.startswith('mem'):
        addr = int(instr.split('[')[1][:-1])
        value = int(value)
        mods = get_mem_updates(addr, mask)
        for m in mods:
          print('setting %d to %d' % (m, value))
          mem[m] = value

  total_mem = sum([x for x in mem.values()])
  print('Total Memory: %d' % (total_mem, ))


main()
