
class Lights(object):
    def __init__(self):
        self._l = []
        for x in range(0, 1000):
            self._l.append([])
            for y in range(0, 1000):
                self._l[x].append(0)


    def brightness_count(self):
        count = 0
        for row in self._l:
            count += sum(row)
        return count

    def on(self, x, y):
        self._l[x][y] += 1

    def off(self, x, y):
        if self._l[x][y] > 0:
          self._l[x][y] -= 1

    def toggle(self, x, y):
        self._l[x][y] += 2

    def _affected_lights(self, x1, y1, x2, y2):
        """Generate all affected lights."""
        for x in range(x1, x2+1):
            for y in range(y1, y2+1):
                yield (x, y)

    def rect_on(self, x1, y1, x2, y2):
        for l in self._affected_lights(x1, y1, x2, y2):
            self.on(*l)

    def rect_off(self, x1, y1, x2, y2):
        for l in self._affected_lights(x1, y1, x2, y2):
            self.off(*l)

    def rect_toggle(self, x1, y1, x2, y2):
        for l in self._affected_lights(x1, y1, x2, y2):
            self.toggle(*l)


with open('input.txt') as f:
    lines = f.readlines()

l = Lights()

for inst in lines:
    if inst.startswith('toggle'):
        (_, p1, _, p2) = inst.split(' ')
        (x1, y1) = [int(x) for x in p1.split(',')]
        (x2, y2) = [int(x) for x in p2.split(',')]
        print('toggling %s %s' % (p1, p2))
        l.rect_toggle(x1, y1, x2, y2)
    else:
        (_, onoff, p1, _, p2) = inst.split(' ')
        (x1, y1) = [int(x) for x in p1.split(',')]
        (x2, y2) = [int(x) for x in p2.split(',')]
        if onoff == 'on':
            print('turning on %s, %s' % (p1, p2))
            l.rect_on(x1, y1, x2, y2)
        elif onoff == 'off':
            print('turning off %s, %s' % (p1, p2))
            l.rect_off(x1, y1, x2, y2)




print ('lights %d' % (l.brightness_count()))
