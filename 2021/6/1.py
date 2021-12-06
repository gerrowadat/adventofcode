#!/usr/bin/env python3

class Fish(object):
    def __init__(self, time_to_spawn):
        self._t = time_to_spawn

    def __str__(self):
        return str(self._t)

    @property
    def time_to_spawn(self):
        return self._t

    def pass_day(self):
        if self._t == 0:
            self._t = 7
        self._t -= 1

class School(object):
    def __init__(self):
        self._f = []

    def __str__(self):
        return ','.join([str(x) for x in self._f])

    @property
    def total_fish(self):
        return len(self._f)

    def add(self, num):
        self._f.append(Fish(num))

    def spawn(self):
        self.add(8)

    def pass_day(self):
        new_fish = 0
        for f in self._f:
            if f.time_to_spawn == 0:
                new_fish += 1
            f.pass_day()
        for i in range(new_fish):
            self.spawn()

def main():
    with open('input.txt') as f:
        raw_fish = f.read().strip().split(',')


    s = School()

    for f in raw_fish:
        s.add(int(f))

    for i in range(80):
        s.pass_day()

    print("Total Fish: %d" % (s.total_fish, ))


if __name__ == '__main__':
    main()
