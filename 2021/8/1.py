#!/usr/bin/env python3


def main():
    with open('input.txt') as f:
        lines = [x.strip() for x in f.readlines()]

    pats = []

    for l in lines:
        (pattern, output) = l.split(' | ')
        pats.append((pattern.split(), output.split()))

    count_1478 = 0

    for (pat, output) in pats:
        simple = [x for x in output if len(x) in (2, 3, 4, 7)]
        count_1478 += len(simple)

    print(count_1478)


if __name__ == '__main__':
    main()
