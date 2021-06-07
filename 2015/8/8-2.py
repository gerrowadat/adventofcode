import sys

def lengthen(line):
    c = 0
    esc = ''
    for c in line:
        if c == '"':
            esc += '\\"'
        elif c == '\\':
            esc += '\\\\'
        else:
            esc += c
    return '"%s"' % (esc, )


def main():
    with open(sys.argv[1]) as f:
        lines = [x.strip() for x in f.readlines()]

    total_regular = 0
    total_long = 0

    for l in lines:
        lengthened = lengthen(l)
        print('%s : %s (%d => %d)' % (l, lengthened, len(l), len(lengthened)))
        total_regular += len(l)
        total_long += len(lengthened)

    print ('Totals: (%d - %d): %d' % (total_long, total_regular, (total_long - total_regular)))

if __name__ == '__main__':
    main()
