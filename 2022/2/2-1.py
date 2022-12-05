#!/usr/bin/env python

import sys

RES = { # player1 move, player2 move, result (0 draw, or 1 or 2)
        ('A', 'X') : 0,
        ('A', 'Y') : 2,
        ('A', 'Z') : 1,
        ('B', 'X') : 1,
        ('B', 'Y') : 0,
        ('B', 'Z') : 2,
        ('C', 'X') : 2,
        ('C', 'Y') : 1,
        ('C', 'Z') : 0
        }

SHAPES = {
        'X': 1,
        'Y': 2,
        'Z': 3
        }

def main():
    global RES
    global SHAPES
    filename = sys.argv[1]
    with open(filename) as f:
        lines = f.readlines()

    score = 0 

    for l in lines:
        (opp, me) = l.strip().split()
        result = RES[(opp, me)]
        if result == 0:
            score += 3 + SHAPES[me]
        elif result == 1:
            score += SHAPES[me]
        elif result == 2:
            score += 6 + SHAPES[me]

    print('Final Score: %d' % (score, ))


if __name__ == '__main__':
    main()
