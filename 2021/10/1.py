#!/usr/bin/env python3


CHUNK_DELIM = {
    ')': '(',
    '}': '{',
    ']': '[',
    '>': '<'
}

ERR_SCORES = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}

def main():
    with open('input.txt') as f:
        lines = [x.strip() for x in f.readlines()]


    err_score = 0

    for l in lines:
        reduced = l
        # reduce uninteresting chunks first
        while True:
            before_len = len(reduced)
            for cl in CHUNK_DELIM:
                empty = '%s%s' % (CHUNK_DELIM[cl], cl)
                reduced = reduced.replace(empty, '')
            if len(reduced) == before_len:
                break

        # Now we should only have opening tokens
        for c in reduced:
            if c in CHUNK_DELIM.keys():
                print('corrupt: %s (unexpected %s)' % (l, c))
                err_score += ERR_SCORES[c]
                break


    print('Error Score: %d' % (err_score, ))


if __name__ == '__main__':
    main()
