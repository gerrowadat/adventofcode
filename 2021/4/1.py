#!/usr/bin/env python3

class Board(object):
    def __init__(self, nums, side_length=5):
        self._b = nums
        self._s = side_length

    def __str__(self):
        ret = ''
        for i in range(0, len(self._b), 5):
            ret += ('%s\n' % (' '.join(self._b[i:i+5])))
        return ret

    def rows(self):
        return [self._b[x:x+self._s] for x in range(0, len(self._b), self._s)]

    def cols(self):
        ret = []
        for top in range(0, self._s):
            col = []
            for idx in range(top, len(self._b), self._s):
                col.append(self._b[idx])
            ret.append(col)
        return ret

    def is_winner(self, drawn):
        for r in self.rows():
            if len([x for x in r if x in drawn]) == len(r):
                return True
        for c in self.cols():
            if len([x for x in c if x in drawn]) == len(c):
                return True
        return False

    def get_unmarked(self, drawn):
        return [x for x in self._b if x not in drawn]


def main():
    with open('input.txt') as f:
        lines = [x.strip() for x in f.readlines()]

    draws = lines[0].split(',')

    boards = []

    for i in range(2, len(lines), 6):
        nums = []
        for j in range(i, i+5):
            nums.extend(lines[j].split())

        boards.append(Board(nums))


    winner = None
    for i in range(len(draws)):
        drawn = draws[:i]
        for b in boards:
            if b.is_winner(drawn):
                winner = b
                print('on [%s] drawn, this board wins: %s' % (drawn, b))
                board_score = sum([int(x) for x in b.get_unmarked(drawn)]) * int(drawn[-1])
                print('Board score: %d' % (board_score, ))
        if winner:
            break


if __name__ == '__main__':
    main()
