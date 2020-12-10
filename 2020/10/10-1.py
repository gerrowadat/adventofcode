def main():
  with open('input.txt') as f:
    lines = sorted([int(x.strip('\n')) for x in f.readlines()])

  jolts = 0
  chain = []

  diff1 = 0
  diff3 = 0

  for idx in range(0, len(lines)):
    diff = lines[idx] - jolts
    if diff == 1:
      diff1 += 1
    if diff == 3:
      diff3 += 1
    jolts = lines[idx]

  # last step to device.
  diff3 += 1

  print('diff1 %d diff3 %d product %d' % (diff1, diff3, (diff1 * diff3)))



  


main()
