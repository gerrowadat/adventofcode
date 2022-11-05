#!/usr/bin/env python

import sys

def reindistance(r, secs):
    reindata = r[1]
    d = 0
    rest = 0
    stamina = reindata[1]
    for i in range(secs):
        if stamina > 0:
            stamina -= 1
            d += reindata[0]
            if stamina == 0:
                rest = reindata[2]
        else:
            if rest > 0:
                rest -= 1
            if rest == 0:
                stamina = reindata[1]

    return d


def main():
    filename = sys.argv[1]
    with open(filename) as f:
        lines = f.readlines()

    reindata = {}

    for l in lines:
        words = l[:-2].split()
        # (speed, stamina, rest)
        reindata.setdefault(words[0], (int(words[3]), int(words[6]), int(words[13])))

    print(reindata)

    secs = 2503

    winner = (None, 0)

    for r in reindata:
        d = reindistance((r, reindata[r]), secs)
        if d > winner[1]:
            winner = (r, d)

    print(winner)



if __name__ == '__main__':
    main()
