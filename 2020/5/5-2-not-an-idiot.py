
def seatnum(p):
  return p.replace('F', '0').replace('B', '1').replace('L', '0').replace('R', '1')

ids = {}
with open('input.txt') as f:
  for l in f:
    num = seatnum(l.strip('\n'))
    row = int(num[:7], 2)
    col = int(num[7:], 2)
    ids[(row * 8) + col] = True

for i in sorted(ids.keys()):
  if (i + 1) not in ids.keys() and (i + 2) in ids.keys():
    print('ID %d is missing and must be yours' % (i + 1))
    col = (i+1) % 8
    row = ((i+1) - col) / 8
    print('Please sit in row %d, column %d' % (row, col))
    break
