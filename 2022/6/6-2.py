#!/usr/bin/env python

import sys

def main():
    filename = sys.argv[1]
    with open(filename) as f:
        lines = f.readlines()

    l = lines[0]

    for i in range(13, len(l)):
        last14 = [*l[i-13:i+1]]
        if len(set(last14)) == len(last14):
            print(last14)
            print('%d' % (i+1, ))
            break



if __name__ == '__main__':
    main()
