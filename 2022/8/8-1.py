#!/usr/bin/env python

import sys


def tree_visible(grid, row, col):

    # Trees on the edge are visible.
    if row == 0 or col == 0 or row == (len(grid) - 1) or col == (len(grid[0]) - 1):
        return True

    viewpoint_up = [grid[x][col] for x in range(0, row)]
    viewpoint_down = [grid[x][col] for x in range(row+1, len(grid))]
    viewpoint_left = [grid[row][x] for x in range(0, col)]
    viewpoint_right = [grid[row][x] for x in range(col+1, len(grid[0]))]

    for v in (viewpoint_up, viewpoint_down, viewpoint_left, viewpoint_right):
        if len([x for x in v if x >= grid[row][col]]) == 0:
            return True

    return False


def main():
    filename = sys.argv[1]
    with open(filename) as f:
        lines = f.readlines()

    trees = [list(l.strip()) for l in lines]

    visible_count = 0

    for row in range(len(trees)):
        for col in range(len(trees[row])):
            if tree_visible(trees, row, col):
                visible_count += 1

    print('%d' % (visible_count, ))


if __name__ == '__main__':
    main()
