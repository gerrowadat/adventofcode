#!/usr/bin/env python3


def main():

    with open("input.txt") as f:
        lines = f.readlines()

    poss = 0

    for l in lines:
        l = l.strip('\n')
        nums = sorted([int(x) for x in l.split()])
        if nums[0] + nums[1] > nums[2]:
            poss += 1

    print('%d possible triangles' % (poss, ))



if __name__ == '__main__':
    main()
