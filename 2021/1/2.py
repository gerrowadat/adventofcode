#!/usr/bin/env python3


def main():
    with open('input.txt') as f:
        lines = f.readlines()

    increases = 0

    sums = [int(lines[x]) + int(lines[x+1]) + int(lines[x+2]) for x in range(len(lines) - 2)]

    for i in range(1, len(sums)):
        if int(sums[i]) > int(sums[i-1]):
            increases += 1

    print('%d increases' % (increases, ))



if __name__ == '__main__':
    main()
