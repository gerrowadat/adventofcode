#!/usr/bin/env python3

def main():
    with open('input.txt') as f:
        lines = [x.strip() for x in f.readlines()]

    output_sum = 0

    for l in lines:
        print(l)
        (pattern, output) = l.split(' | ')
        pattern = pattern.split()
        output = output.split()

        known_pat = {}
        known_pat[1] = [x for x in pattern if len(x) == 2][0]
        print('#1 is %s' % known_pat[1])
        known_pat[4] = [x for x in pattern if len(x) == 4][0]
        print('#4 is %s' % known_pat[4])
        known_pat[7] = [x for x in pattern if len(x) == 3][0]
        print('#7 is %s' % known_pat[7])
        known_pat[8] = [x for x in pattern if len(x) == 7][0]
        print('#8 is %s' % known_pat[8])

        known_seg = {}
        # 0 doesn't appear in digit 1, does in 7
        known_seg[0] = [x for x in known_pat[7] if x not in known_pat[1]][0]
        print('0 is %s' % known_seg[0])
        # Segment 5 is always lit except for on digit 2, so will appear exactly 9 times.
        all_seg = ''.join(pattern)
        known_seg[5] = [x for x in all_seg if all_seg.count(x) == 9][0]
        print('5 is %s' % known_seg[5])
        # Segment 2 is the other segment of digit 1
        known_seg[2] = [x for x in known_pat[1] if x != known_seg[5]][0]
        print('2 is %s' % known_seg[2])
        # digit 6 is missing only segment 2
        known_pat[6] = [x for x in pattern if len(x) == 6 and known_seg[2] not in x][0]
        print('#6 is %s' % known_pat[6])
        # Digit 2 has length 5 and missing segment 5
        known_pat[2] = [x for x in pattern if len(x) == 5 and known_seg[5] not in x][0]
        print('#2 is %s' % known_pat[2])
        # Digit 3 has length 5 and 0,2,5
        known_pat[3] = [x for x in pattern if len(x) == 5 and (known_seg[0] in x and known_seg[2] in x and known_seg[5] in x)][0]
        print('#3 is %s' % known_pat[3])
        # Digit 5 has length 5 and missing segment 2
        known_pat[5] = [x for x in pattern if len(x) == 5 and known_seg[2] not in x][0]
        print('#5 is %s' % known_pat[5])
        # Just 9 and 0 to go. I am very good at programming.
        # Segment 4 is not in 3, 4 or 5
        known_seg[4] = [x for x in 'abcdefg' if x not in known_pat[3] and x not in known_pat[4] and x not in known_pat[5]][0]
        print('4 is %s' % known_seg[4])
        known_pat[9] = [x for x in pattern if len(x) == 6 and known_seg[4] not in x][0]
        print('#9 is %s' % known_pat[9])
        known_pat[0] = [x for x in pattern if x not in known_pat.values()][0]
        print('#0 is %s' % known_pat[0])

        real_output = ''
        for o in output:
            real_output += str([x for x in known_pat.keys() if sorted(known_pat[x]) == sorted(o)][0])

        output_sum += int(real_output)

    print('Output sum: %d' % (output_sum))




if __name__ == '__main__':
    main()
