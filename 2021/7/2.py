#!/usr/bin/env python3

def main():
    with open('input.txt') as f:
        crabs = [int(x) for x in f.read().strip().split(',')]

    # I am still a one-liner smartypants and will never get my come-uppance.
    print('Min fuel: %d' % (min([sum([ (((abs(y - x)**2)+abs(y - x)) / 2) for y in crabs]) for x in range(min(crabs), max(crabs)+1)])))

if __name__ == '__main__':
    main()
