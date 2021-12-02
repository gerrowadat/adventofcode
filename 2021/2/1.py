#!/usr/bin/env python3


def main():
    with open('input.txt') as f:
        lines = f.readlines()

    horizontal = 0
    depth = 0

    for l in lines:
        (cmd, num) = l.split(' ')
        num = int(num)
        if cmd == 'forward':
            horizontal += num
        elif cmd == 'down':
            depth += num
        elif cmd == 'up':
            depth -= num
        else:
            print("Don't know how to <%s>" % (cmd, ))


    print('h %d d %d Total %d' % (horizontal, depth, (horizontal * depth)))


if __name__ == '__main__':
    main()
