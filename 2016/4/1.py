#!/usr/bin/env python3

def get_checksum(text):
    # Build an alpha lookup table {letter: frequency}
    table = {}
    for ch in text:
        if ch.isalpha():
            table[ch] = table.get(ch, 0) + 1

    # Step down from top ranked letters, appending in alpha order to the checksum
    freq = max(table.values())
    check = ''
    while len(check) < 5:
        k = sorted([x for x in table.keys() if table[x] == freq])
        check += ''.join(k)
        freq -= 1

    return check[:5]

def main():
    with open('input.txt') as f:
        lines = f.readlines()

    sector_sum = 0

    for l in lines:
        checksum = l[-7:-2]
        sector = int(l[-11:-8])
        name = l[:-12]
        our_checksum = get_checksum(name)
        print('%s : %s/%s (%d)' % (name, checksum, our_checksum, sector))
        if our_checksum == checksum:
            sector_sum += sector

    print ('sector sum: %d' % (sector_sum, ))


if __name__ == '__main__':
    main()
