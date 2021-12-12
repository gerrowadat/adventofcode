#!/usr/bin/env python3

class Dumbo(object):
    def __init__(self, x, y, energy):
        self._x = int(x)
        self._y = int(y)
        self._e = int(energy)

    def __str__(self):
        return '(%d, %d): %d' % (self._x, self._y, self._e)

    def __hash__(self):
        return hash('%d,%d' % (self._x, self._y))

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @property
    def energy(self):
        return self._e

    def inc(self):
        self._e += 1

    def flash(self):
        self._e = 0


class Grid(object):
    def __init__(self, xlen, ylen):
        self._g = []
        self._xlen = xlen
        self._ylen = ylen
        # number of flashes.
        self._f = 0

    def __str__(self):
        ret = ''
        for i in range(self._ylen):
            for j in range(self._xlen):
                ret += str(self.at(j, i))
            ret += '\n'
        return ret

    @property
    def dumbo_count(self):
        return self._xlen * self._ylen
    @property
    def flashes(self):
        return self._f

    def add(self, x, y, energy):
        self._g.append(Dumbo(x, y, energy))

    def at(self, x, y):
        return [p for p in self._g if p.x == x and p.y == y][0].energy

    def step(self):
        for dumbo in self._g:
            dumbo.inc()
        # Keep updating until no more flashes happen.
        (updates, flashers) = self._process()
        for f in flashers:
            f.flash()
        return len(flashers)

    def _neighbours(self, p):
        return [n for n in self._g if n.x in (p.x-1, p.x, p.x+1) and n.y in (p.y-1, p.y, p.y+1) and (n != p)]

    def _process(self):
        updates = 0
        flashers = []
        for dumbo in self._g:
            if dumbo.energy > 9 and dumbo not in flashers:
                flashers.append(dumbo)
                dumbo.flash()
                self._f += 1
                for n in self._neighbours(dumbo):
                    n.inc()
                    (new_updates, new_flashers) = self._process()
                    updates += new_updates
                    flashers.extend(new_flashers)
        return (updates, flashers)

def main():
    with open('input.txt') as f:
        lines = [x.strip() for x in f.readlines()]

    g = Grid(len(lines[0]), len(lines))

    for l in range(len(lines)):
        for ch in range(len(lines[l])):
            g.add(ch, l, lines[l][ch])

    print(str(g))

    step_count = 0
    while True:
        flasher_count = g.step()
        step_count += 1
        if flasher_count == g.dumbo_count:
            print('steps until full flash: %d' % (step_count))
            break


    print(str(g))

    print ('Flashes: %d' % (g.flashes))


if __name__ == '__main__':
    main()
