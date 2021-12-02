#!/usr/bin/env python3


def main():
    with open('input.txt') as f:
        lines = f.readlines()

    horizontal = 0
    depth = 0
    aim = 0

    for l in lines:
        (cmd, num) = l.split(' ')
        num = int(num)
        if cmd == 'forward':
            horizontal += num
            depth += (num * aim)
        elif cmd == 'down':
            aim += num
        elif cmd == 'up':
            aim -= num
        else:
            print("Don't know how to <%s>" % (cmd, ))


    print('h %d d %d Total %d' % (horizontal, depth, (horizontal * depth)))


if __name__ == '__main__':
    main()
