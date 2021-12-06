#!/usr/bin/env python3

def main():
    with open('input.txt') as f:
        raw_fish = [int(x) for x in f.read().strip().split(',')]

    all_fish = {x: 0 for x in range(9)}

    for raw in raw_fish:
        all_fish[raw] += 1

    for _ in range(256):
        new_fish = {x: 0 for x in range(9)}
        for fish_age in all_fish:
            if fish_age == 0:
                new_fish[8] += all_fish[0]
                new_fish[6] += all_fish[0]
            else:
                new_fish[fish_age-1] += all_fish[fish_age]

        all_fish = new_fish

    print("Total Fish: %d" % (sum(all_fish.values())))


if __name__ == '__main__':
    main()
