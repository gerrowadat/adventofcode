#!/usr/bin/env python3


def reduce(nums, digit=0, criterion=lambda x, y: len(x) >= (len(y) / 2)):
    if len(nums) <= 1:
        return nums

    ones = [x[digit] for x in nums if x[digit] == '1']

    if criterion(ones, nums):
            return reduce([x for x in nums if x[digit] == '1'], digit+1, criterion)
    else:
            return reduce([x for x in nums if x[digit] == '0'], digit+1, criterion)


def main():
    with open('input.txt') as f:
        lines = [x.strip() for x in f.readlines()]

    # Deep copy lines for each reduction
    gen = reduce([x for x in lines])
    scrubber = reduce([x for x in lines], criterion=lambda x, y: len(x) < (len(y) / 2))

    print('gen %s scrubber %s life %d' % (gen[0], scrubber[0], (int(gen[0], 2) * int(scrubber[0], 2))))


if __name__ == '__main__':
    main()
