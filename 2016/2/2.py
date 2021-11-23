#!/usr/bin/env python3

_GRID = ['XXXXXXX',
         'XXX1XXX',
         'XX234XX',
         'X56789X',
         'XXABCXX',
         'XXXDXXX',
         'XXXXXXX']

_GRID.reverse()  # Easier to visualise this way, but 0,0 is bottom left.

def key_from_coords(x, y):
    if y == 0:
        return 7 + x
    elif y == 1:
        return 4 + x
    else:
        return 1 + x

class KeypadPicker(object):
    def __init__(self):
        print(_GRID)
        # Start at 5
        self._x = 1
        self._y = 3

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @property
    def active_key(self):
        return _GRID[self.y][self.x]

    def _step(self, direction):
        print ('stepping %s from %d,%d' % (direction, self.x, self.y))
        if direction == 'U':
            if _GRID[self.y + 1][self.x] == 'X':
                return
            self._y += 1
        elif direction == 'D':
            if _GRID[self.y - 1][self.x] == 'X':
                return
            self._y -= 1
        elif direction == 'R':
            if _GRID[self.y][self.x+1] == 'X':
                return
            self._x += 1
        elif direction == 'L':
            if _GRID[self.y][self.x - 1] == 'X':
                return
            self._x -= 1

    def move(self, directions):
        for d in directions:
            self._step(d)
        print('%s => %d,%d' % (directions, self.x, self.y))
        return (self.x, self.y)

def main():
    with open('input.txt') as f:
        instructions = [x.strip() for x in f.readlines()]

    kp = KeypadPicker()

    comb = ''

    for instr in instructions:
        print('processing %s' % (instr))
        kp.move(instr)
        print ('Active key: %s' % (kp.active_key))
        comb += kp.active_key

    print('Combination is %s' % (comb))




if __name__ == '__main__':
    main()
