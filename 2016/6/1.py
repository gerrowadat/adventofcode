#!/usr/bin/env python3


def main():
    with open('input.txt') as f:
        lines = [x.strip() for x in f.readlines()]

    msg = ''

    for col in range(len(lines[0])):
        freqs = {}
        for ch in [x[col] for x in lines]:
            freqs[ch] = freqs.get(ch, 0) + 1
        msg += sorted(freqs.keys(), key=lambda x: freqs[x])[-1]

    print(msg)

if __name__ == '__main__':
    main()
