#!/usr/bin/env python

import sys

def molecule_subs(orig, before, after):
    start = 0
    if orig.startswith(before):
        #print ('found at start, returning %s + %s ' % (before, orig[len(before):]))
        yield after + orig[len(before):]
        start = len(before)
    for i in range(start, len(orig)):
        cmp = orig[i:i+len(before)]
        if cmp == before:
            #print('found %s at index %d' % (cmp, i))
            #print ('ret %s + %s + %s' % (orig[:i], after,  orig[i+len(before):]))
            yield orig[:i] + after + orig[i+len(before):]


def main():
    filename = sys.argv[1]
    with open(filename) as f:
        lines = f.readlines()

    subs_lines = lines[:-2]
    med = lines[-1].strip()

    subs = []


    for s in subs_lines:
        subs.append(s.strip().split(' => '))


    all_med = set()

    for s in subs:
        #print('Getitng subs for (%s, %s)' % (s[0], s[1]))
        for result in molecule_subs(med, s[0], s[1]):
            #print(result)
            all_med.add(result)

    print('%d' % (len(all_med)))


if __name__ == '__main__':
    main()
