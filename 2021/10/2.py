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

COMPLETION_SCORES = {
    '(': 1,
    '[': 2,
    '{': 3,
    '<': 4
}


def main():
    with open('input.txt') as f:
        lines = [x.strip() for x in f.readlines()]


    err_score = 0
    complete_scores = []

    for l in lines:
        corrupt = False
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
                print('Corrupt: %s (unexpected %s)' % (l, c))
                err_score += ERR_SCORES[c]
                corrupt = True
                break

        if not corrupt:
            # Incomplete. Complete by adding the 'reverse' of the reduced line.
            this_score = 0
            for ch in "".join(reversed(reduced)):
                this_score *= 5
                this_score += COMPLETION_SCORES[ch]

            print('Incomplete: %s (reduced to "%s", score %d)' % (l, reduced, this_score))

            complete_scores.append(this_score)


    print('Total Error Score: %d' % (err_score, ))
    index = int(((len(complete_scores) - 1) / 2))
    print('Middle Completion score: %d' % (sorted(complete_scores)[index]))


if __name__ == '__main__':
    main()
