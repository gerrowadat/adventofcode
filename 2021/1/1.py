#!/usr/bin/env python3


def main():
    with open('input.txt') as f:
        lines = f.readlines()

    increases = 0

    for i in range(1, len(lines)):
        if int(lines[i]) > int(lines[i-1]):
            increases += 1

    print('%d increases' % (increases, ))



if __name__ == '__main__':
    main()
