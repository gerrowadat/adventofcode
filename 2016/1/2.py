#!/usr/bin/env python3


_DIRS = ('n', 'e', 's', 'w')


class GridJourney(object):
    def __init__(self):
        self._x = 0
        self._y = 0
        self._face = 0 # north
        self._history = ([0,0])

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @property
    def facing(self):
        return _DIRS[self._face]

    def _step(self):
        # Take one step forward.
        if self.facing == 'n':
            self._y += 1
        elif self.facing == 's':
            self._y -= 1
        elif self.facing == 'e':
            self._x += 1
        elif self.facing == 'w':
            self._x -= 1

        if self._visit(self.x, self.y):
            print('been here before: %s' % ([self.x, self.y]))


    def _visit(self, x, y):
        # Add [x,y] to history, returning True if we've visited already
        if [x, y] in self._history:
            return True
        else:
            self._history.append([x, y])
            return False

    def turn(self, direction):
        if direction == 'R':
            self._face = (self._face + 1) % 4
        elif direction == 'L':
            self._face -= 1

    def move(self, steps):
        for s in range(steps):
            self._step()




def main():
    with open('input.txt') as f:
        line = f.read().strip('\n')

    steps = line.split(', ')

    gj = GridJourney()

    for step in steps:
        direction = step[0]
        distance = int(step[1:])

        gj.turn(direction)
        gj.move(distance)


if __name__ == '__main__':
    main()
