#!/usr/bin/env python3


def main():
    with open('input.txt') as f:
        lines = [x.strip() for x in f.readlines()]

    gamma = ''
    epsilon = ''

    for digit in range(len(lines[0])):
        ones = [x[digit] for x in lines if x[digit] == '1']
        if len(ones) > (len(lines) / 2):
            gamma += '1'
            epsilon += '0'
        else:
            gamma += '0'
            epsilon += '1'

    print ('gamma %s epsilon %s consumption %d' % (gamma, epsilon, (int(gamma, 2) * int(epsilon, 2))))



if __name__ == '__main__':
    main()
