def main():
  with open('input.txt') as f:
    ts = int(f.readline().strip('\n'))
    buses = [int(x) for x in f.readline().strip('\n').split(',') if x != 'x']

  min_wait = (None, None)
  for b in buses:
    next_arrival = (ts / b + 1) * b
    if next_arrival % ts < min_wait[1] or min_wait[1] is None:
      min_wait = (b, next_arrival % ts)

  print('Min wait is for bus %d in %d minutes' % min_wait)
  print('Result: %d' % (min_wait[0] * min_wait[1]))


main()
