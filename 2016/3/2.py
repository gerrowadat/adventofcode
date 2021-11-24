#!/usr/bin/env python3

def get_triangles(grid):
    for x in (0, 1, 2):
        for y in range(0, len(grid) - 2, 3):
            yield sorted([grid[y][x], grid[y+1][x], grid[y+2][x]])

def main():

    with open("input.txt") as f:
        lines = f.readlines()

    grid = []

    for l in lines:
        l = l.strip('\n')
        nums = [int(x) for x in l.split()]
        grid.append(nums)

    valid = 0

    for tri in get_triangles(grid):
        print('tri: %s' % (tri,))
        if int(tri[0]) + int(tri[1]) > int(tri[2]):
            valid += 1

    print('%d valid triangles' % (valid, ))

if __name__ == '__main__':
    main()
