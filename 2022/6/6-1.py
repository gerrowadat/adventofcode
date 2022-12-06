#!/usr/bin/env python

import sys

def main():
    filename = sys.argv[1]
    with open(filename) as f:
        lines = f.readlines()

    l = lines[0]

    for i in range(3, len(l)):
        last4 = [*l[i-3:i+1]]
        if len(set(last4)) == len(last4):
            print(last4)
            print('%d' % (i+1, ))
            break



if __name__ == '__main__':
    main()
