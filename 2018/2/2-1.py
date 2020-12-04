def char_counts(word):
    word = word.strip('\n')
    # <char> : <count>
    counts = {}
    for c in word:
        if c not in counts:
            counts[c] = 1
        else:
            counts[c] += 1
    return counts

def main():
    with open('2018/2/input.txt') as f:
        raw_lines = f.readlines()

    has_2 = 0
    has_3 = 0
    # <number of common letters> : <count of strings with that number>
    for l in raw_lines:
        c = char_counts(l)
        if 2 in c.values():
            has_2 += 1
        if 3 in c.values():
            has_3 += 1

    print ('Checksum: %d' % (has_2 * has_3))

main()