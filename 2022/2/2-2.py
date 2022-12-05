#!/usr/bin/env python

import sys

PLAYS = { # player1 move, result, Player 2 move
        ('A', 'X') : 'Z',
        ('A', 'Y') : 'X',
        ('A', 'Z') : 'Y',
        ('B', 'X') : 'X',
        ('B', 'Y') : 'Y',
        ('B', 'Z') : 'Z',
        ('C', 'X') : 'Y',
        ('C', 'Y') : 'Z',
        ('C', 'Z') : 'X'
        }

SHAPES = {
        'X': 1,
        'Y': 2,
        'Z': 3
        }

def main():
    global PLAYS
    global SHAPES
    filename = sys.argv[1]
    with open(filename) as f:
        lines = f.readlines()

    score = 0 

    for l in lines:
        (opp, play) = l.strip().split()
        me = PLAYS[(opp, play)]

        if play == 'Y':
            score += 3
        elif play == 'Z':
            score += 6

        score += SHAPES[me]

    print('Final Score: %d' % (score, ))


if __name__ == '__main__':
    main()
