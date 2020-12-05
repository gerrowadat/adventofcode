import hashlib

inp = 'ckczppom'

num = 1

while True:
  h = hashlib.md5()
  plain = '%s%d' % (inp, num)
  h.update(plain)
  if str(h.hexdigest()).startswith('00000'):
    print('Lowest: %d' % (num, ))
    break
  num += 1

