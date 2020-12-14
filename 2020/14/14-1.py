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
        masked_value = apply_mask(value, mask)
        print('setting %d to %d (after mask: %d)' % (addr, value, masked_value))
        mem[addr] = masked_value

  total_mem = sum([x for x in mem.values()])
  print('Total Memory: %d' % (total_mem, ))




main()
