import sys

def shorten(line):
    noquotes = line[1:len(line)-1]
    print ('Inspecting %s' % (noquotes))
    short = ''
    c = 0
    while c < len(noquotes):
        print('looking at %s' % (noquotes[c]))
        if noquotes[c] != '\\':
            short += noquotes[c]
            c += 1
        else:
            if c < len(noquotes) and noquotes[c+1] == '"':
                short += '"'
                c += 2
            elif c < len(noquotes) and noquotes[c+1] == '\\':
                short += '\\'
                c += 2
            elif c < len(noquotes)-2 and noquotes[c+1] == 'x':
                hexcode = noquotes[c+2:c+3]
                newchar = chr(int(hexcode, 16))
                short += newchar
                c += 4
            else:
                c += 1

    return short

def main():
    with open(sys.argv[1]) as f:
        lines = [x.strip() for x in f.readlines()]

    total_full = 0
    total_short = 0

    for l in lines:
        short = shorten(l)
        print('%s : %s (%d => %d)' % (l, short, len(l), len(short)))
        total_full += len(l)
        total_short += len(short)

    print ('Totals: (%d - %d): %d' % (total_full, total_short, (total_full - total_short)))

if __name__ == '__main__':
    main()
