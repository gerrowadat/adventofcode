#!/usr/bin/env python

import sys


def scenic_score(grid, row, col):

    view_up = [grid[x][col] for x in range(row-1, -1, -1)]
    view_down = [grid[x][col] for x in range(row+1, len(grid))]
    view_left = [grid[row][x] for x in range(col-1, -1, -1)]
    view_right = [grid[row][x] for x in range(col+1, len(grid[0]))]

    views = []

    for v in (view_up, view_down, view_left, view_right):
        view = 0
        for s in v:
            view += 1
            if s >= grid[row][col]:
                break
        views.append(view)

    if 0 in views:
        return 0

    ret = 1
    for x in views:
        ret = ret * x

    return ret

def main():
    filename = sys.argv[1]
    with open(filename) as f:
        lines = f.readlines()

    trees = [list(l.strip()) for l in lines]

    max_score = 0

    for row in range(len(trees)):
        for col in range(len(trees[row])):
            vis = scenic_score(trees, row, col)
            if vis > max_score:
                max_score = vis

    print('%d' % (max_score, ))


if __name__ == '__main__':
    main()
