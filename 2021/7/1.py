#!/usr/bin/env python3

def fuel_to_pos(pos, crabs):
    return sum([abs(x - pos) for x in crabs])

def main():
    with open('input.txt') as f:
        crabs = [int(x) for x in f.read().strip().split(',')]

    print('Min fuel: %d' % (min([fuel_to_pos(x, crabs) for x in range(min(crabs), max(crabs)+1)])))

if __name__ == '__main__':
    main()
