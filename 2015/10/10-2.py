import sys

def say(inp):
    if len(inp) == 1:
        return '1' + inp

    out = ''
    c = 1
    curr = inp[0]
    curr_count = 1
    while c < len(inp):
        if inp[c] == curr:
            curr_count += 1
            c += 1
        elif inp[c] != curr:
            out += '%s%s' % (curr_count, curr)
            curr  = inp[c]
            curr_count = 1
            c += 1


    out += '%s%s' % (curr_count, curr)

    return out


def main():
    inp = sys.argv[1]
    for i in range(50):
        inp = say(inp)

    print(len(inp))


if __name__ == '__main__':
    main()
