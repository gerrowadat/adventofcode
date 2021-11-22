#!/usr/bin/env python3


_DIRS = ('U', 'R', 'D', 'L')

def key_from_coords(x, y):
    if y == 0:
        return 7 + x
    elif y == 1:
        return 4 + x
    else:
        return 1 + x

class KeypadPicker(object):
    def __init__(self):
        # Start at 5, [0,0] is 7
        self._x = 1
        self._y = 1

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @property
    def active_key(self):
        return key_from_coords(self.x, self.y)

    def _step(self, direction):
        print ('stepping %s from %d,%d' % (direction, self.x, self.y))
        if direction == 'U':
            if self.y == 2:
                return
            self._y += 1
        elif direction == 'D':
            if self.y == 0:
                return
            self._y -= 1
        elif direction == 'R':
            if self.x == 2:
                return
            self._x += 1
        elif direction == 'L':
            if self.x == 0:
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
        print ('Active key: %d' % (kp.active_key))
        comb += str(kp.active_key)

    print('Combination is %s' % (comb))




if __name__ == '__main__':
    main()
