#!/usr/bin/env python

import sys


class Sue(object):
    def __init__(self):
        self._id = None
        self._attrs = {}

    def __str__(self):
        return 'Sue %d: %s' % (
                self.id, ', '.join(
                    ['%s: %s' % (
                        x, self._attrs[x]) for x in self._attrs.keys()]))

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, val):
        self._id = val

    @property
    def attrs(self):
        return self._attrs.keys()

    def attr(self, key):
        return self._attrs.get(key, None)

    def set_attr(self, key, val):
        self._attrs[key] = val

    def match(self, partial):
        for ak in partial.attrs:
            if self.attr(ak) is not None and self.attr(ak) != partial.attr(ak):
                return False
        for ak in self.attrs:
            if partial.attr(ak) is not None and (
                    self.attr(ak) != partial.attr(ak)):
                return False
        return True


def main():
    filename = sys.argv[1]
    with open(filename) as f:
        lines = f.readlines()

    sues = []

    for line in lines:
        words = line.split()
        s = Sue()
        s.id = int(words[1][:-1])

        for i in range(2, len(words), 2):
            attr = words[i][:-1]
            val = int(words[i+1].replace(',', ''))
            s.set_attr(attr, val)

        sues.append(s)

    mystery_sue = Sue()
    mystery_sue.set_attr('children', 3)
    mystery_sue.set_attr('cats', 7)
    mystery_sue.set_attr('samoyeds', 2)
    mystery_sue.set_attr('pomeranians', 3)
    mystery_sue.set_attr('akitas', 0)
    mystery_sue.set_attr('vizslas', 0)
    mystery_sue.set_attr('goldfish', 5)
    mystery_sue.set_attr('trees', 3)
    mystery_sue.set_attr('cars', 2)
    mystery_sue.set_attr('perfumes', 1)

    for s in sues:
        if s.match(mystery_sue):
            print('Sue #%s matches.' % (s.id, ))


if __name__ == '__main__':
    main()
