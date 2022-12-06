#!/usr/bin/env python

import sys

class Cargo(object):
    def __init__(self):
        self._s = {}

    def __str__(self):
        ret = ''
        for s in self._s:
            ret += '%s: %s\n' % (s, ' '.join(self._s[s]))
        return ret

    def add_stack(self, name):
        self._s[name] = []

    def add_item(self, dst, item):
        if dst not in self._s.keys():
            raise ValueError('no such stack: %s' % (dst,))
        self._s[dst].append(item)


    def move(self, src, dst):
        if src not in self._s.keys() or dst not in self._s.keys():
            raise ValueError('no such stack: %s -> %s' % (src, dst))
        item = self._s[src].pop()
        if item:
            self._s[dst].append(item)

    def move_several(self, count, src, dst):
        if src not in self._s.keys() or dst not in self._s.keys():
            raise ValueError('no such stack: %s -> %s' % (src, dst))
        lift = []
        for i in range(count):
            lift.append(self._s[src].pop())
        lift.reverse()
        self._s[dst].extend(lift)


    def tops(self):
        return ''.join([s[-1] for s in self._s.values()])

def main():
    filename = sys.argv[1]
    with open(filename) as f:
        lines = f.readlines()

    
    # Find the number of stacks first.
    numstacks = 0
    # ...also the line# at which we stop seeing stack definitions
    stack_idx = 0
    for i in range(len(lines)):
        if lines[i].strip() == '':
            stacklabels = lines[i-1]
            numstacks = len(lines[i-1].split())
            stack_idx = i-2
            break

    print('There are %d stacks' % (numstacks, ))

    c = Cargo()
    for i in range(numstacks):
        c.add_stack(i+1)


    # populate the stacks
    for i in range(stack_idx, -1, -1):
        stackline = lines[i]
        for s in range(numstacks):
            idx = 1 + (4*s)
            if lines[i][idx] != ' ':
                c.add_item(s+1, lines[i][idx])


    print(c)

    # process moves.
    for i in range(stack_idx+3, len(lines)):
        words = lines[i].split()
        count = int(words[1])
        src = int(words[3])
        dst = int(words[5])

        c.move_several(count, src, dst)


    print(c)
    print(c.tops())

if __name__ == '__main__':
    main()
