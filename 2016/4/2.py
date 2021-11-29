#!/usr/bin/env python3

import string

def shift_name(text, shift):
  # This omits spaces but who cares we're grepping the answer out anyway.
  new_text = [string.ascii_lowercase[((ord(x) - ord('a')) + shift) % 26] for x in text if x.isalpha()]
  return ''.join(new_text)

def main():
    with open('input.txt') as f:
        lines = f.readlines()

    for l in lines:
        checksum = l[-7:-2]
        sector = int(l[-11:-8])
        name = l[:-12]
        print('%d %s' % (sector, shift_name(name, sector)))



if __name__ == '__main__':
    main()
