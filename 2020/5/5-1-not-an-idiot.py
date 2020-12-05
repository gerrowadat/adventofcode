
def seatnum(p):
  return p.replace('F', '0').replace('B', '1').replace('L', '0').replace('R', '1')

max_id = 0
with open('input.txt') as f:
  for l in f:
    num = seatnum(l.strip('\n'))
    row = int(num[:7], 2)
    col = int(num[7:], 2)
    p_id = (row * 8) + col
    if p_id > max_id:
      max_id = p_id

print('Highest ID: %d' % (max_id, ))
