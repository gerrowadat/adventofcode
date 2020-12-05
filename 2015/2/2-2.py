def required_paper(l, w, h):
  areas = [l*w, w*h, h*l]
  return (2 * ((l*w) + (w*h) + (h*l))) + sorted(areas)[0]

def required_ribbon(l, w, h):
  (l, w, h) = (int(l), int(w), int(h))
  (short1, short2) = sorted([l, w, h])[:2]
  return (2 * (short1 + short2)) + (l * w * h)

with open('input.txt') as f:
  total = 0
  for line in f:
    (l, w, h) = [int(x) for x in line.strip('\n').split('x')]
    total += required_ribbon(l, w, h)
    print('%s : %d' % (line.strip('\n'), required_paper(l, w, h)))

print ('Total ribbon: %d' % (total, ))
