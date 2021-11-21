#!/usr/bin/env python3

with open('input.txt') as f:
    line = f.read().strip('\n')

steps = line.split(', ')

# Possible directions, turning right each time.
dirs = ('n', 'e', 's', 'w')

pos = [0, 0]
# Initially facing north
face = 0



for step in steps:
    direction = step[0]
    distance = int(step[1:])
    if direction == 'R':
        face = (face + 1) % 4
    elif direction == 'L':
        face -= 1

    if dirs[face] == 'n':
        pos[1] += distance
    elif dirs[face] == 's':
        pos[1] -= distance
    elif dirs[face] == 'e':
        pos[0] += distance
    elif dirs[face] == 'w':
        pos[0] -= distance
    print('now facing %s at %s' % (dirs[face], pos))

print('pos: %s' % (pos, ))
print ('distance: %d' % (abs(pos[0]) + abs(pos[1])))

