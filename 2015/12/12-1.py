#!/usr/bin/env python

import sys

def main():
    filename = sys.argv[1]
    with open(filename) as f:
        lines = f.readlines()
    raw_doc = ''.join(lines)

    raw_doc = raw_doc.replace(',', ' ')
    raw_doc = raw_doc.replace(':', ' ')
    raw_doc = raw_doc.replace('[', ' ')
    raw_doc = raw_doc.replace(']', ' ')
    raw_doc = raw_doc.replace('{', ' ')
    raw_doc = raw_doc.replace('}', ' ')
    raw_doc = raw_doc.replace('"', ' ')

    total = 0

    for tok in raw_doc.split():
        print('tok: %s' % (tok, ))
        if tok.isnumeric() or tok[0] == '-' and tok[1:].isnumeric():
            total += int(tok)

    print('Total: %d' % (total))


if __name__ == '__main__':
    main()
