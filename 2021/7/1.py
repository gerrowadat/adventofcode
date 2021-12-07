#!/usr/bin/env python3

def main():
    with open('input.txt') as f:
        crabs = [int(x) for x in f.read().strip().split(',')]

    print('Min fuel: %d' % (min([sum([abs(y - x) for y in crabs]) for x in range(min(crabs), max(crabs)+1)])))

if __name__ == '__main__':
    main()
