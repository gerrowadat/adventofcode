def has_sum(i, nums):
  for n in nums:
    sums = [x for x in nums if x != n and x + n == i]
    if sums:
      return True

def main():

  preamble = 25

  window = []

  with open('input.txt') as f:
    # Get our initial preamble window
    for p in range(0, preamble):
      window.append(int(f.readline().strip('\n')))

    for l in f:
      l = int(l.strip('\n'))
      if not has_sum(int(l), window):
        print('%d does not have a sum pair in %s' % (l, window))
        return
      window.append(l)
      window.pop(0)

    print('Input valid')

main()
