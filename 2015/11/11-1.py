import sys


def increment(inp):
    lsd = inp[-1]
    lettercode = ord(lsd)
    lettercode += 1
    if lettercode > 122:  #  z
        lettercode = 97   #  a
        if len(inp) == 1:
            return 'a' + chr(lettercode)

        return increment(inp[:-1]) + chr(lettercode)
    else:
        return inp[:-1] + chr(lettercode)


def has_straight(inp):
    if len(inp) < 3:
        return False

    prev = None
    run = 0

    target = 3
    for c in range(len(inp)):
        if prev is None:
            prev = inp[c]
            run = 1
        elif ord(inp[c]) == (ord(prev) + 1):
            run += 1
            if run == target:
                return True
            prev = inp[c]
        else:
            prev = inp[c]
            run = 1
    return False


def no_invalid_chars(inp):
    for invalid in ['i', 'o', 'l']:
        if invalid in inp:
            return False
    return True


def has_pairs(inp):
    pair_loc = []
    for c in range(len(inp)):
        if c == len(inp)-1:
            continue
        if inp[c+1] == inp[c]:
            pair_loc.append(c)
    # max difference betwen all pair locations can't be 1
    max_diff = 0
    for p in pair_loc:
        for i in pair_loc:
            if abs(p-i) > max_diff:
                max_diff = abs(p-i)
    if max_diff >= 2:
        return True
    return False


def valid_pass(newp):
    if has_straight(newp) and no_invalid_chars(newp) and has_pairs(newp):
        return True
    return False


def main():
    inp = sys.argv[1]

    while not valid_pass(inp):
        inp = increment(inp)
        print('trying %s...' % (inp, ))

    print('new password: %s' % (inp,))

if __name__ == '__main__':
    main()
