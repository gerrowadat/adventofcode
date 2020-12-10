def main():
  with open('input.txt') as f:
    lines = sorted([int(x.strip('\n')) for x in f.readlines()])

  vals = [0]
  vals.extend(lines)
  vals.append(lines[-1] + 3)

  c = dict([(x, 0) for x in range(0, len(vals))])
  c[0] = 1

  print(vals)
  for i in range(0, len(vals)):
    for j in range(1, min(4, len(vals) - i)):
      if vals[i+j] < vals[i] + 4:
        c[i+j] += c[i]

  print('Paths: %s' % (c[len(vals)-1], ))


main()
