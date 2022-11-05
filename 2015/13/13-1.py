#!/usr/bin/env python

import sys
import itertools


def pair_change(changes, a, b):
    return (changes[a][b] + changes[b][a])

def permutation_change(perm, changes):
    change = 0
    for i in range(len(perm)):
        if i == len(perm) -1:
            change += pair_change(changes, perm[-1], perm[0])
        else:
            change += pair_change(changes, perm[i], perm[i+1])
    return change

def main():
    filename = sys.argv[1]
    with open(filename) as f:
        lines = f.readlines()

    changes = {}

    for l in lines:
        words = l[:-2].split()
        if words[0] not in changes.keys():
            changes[words[0]] = {}
        if words[2] == 'gain':
            changes[words[0]][words[10]] = int(words[3])
        else:
            # 'lose'
            changes[words[0]][words[10]] = int('-' + words[3])

    results = {}

    highest = 0

    for p in itertools.permutations(changes.keys()):
        res = permutation_change(p, changes)
        results[p] = res
        if res > highest:
            highest = res


    print(results)
    print('highest: %d' % (highest))


if __name__ == '__main__':
    main()
