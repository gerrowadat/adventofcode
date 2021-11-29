#!/usr/bin/env python3

import hashlib

def main():
    door = 'ugkcyxxp'
    password = [None] * 8

    inc = -1
    while True:
        inc += 1
        h = hashlib.md5()
        text = '%s%d' % (door, inc)
        b = text.encode('utf-8')
        h.update(b)
        if h.hexdigest().startswith('00000'):
            index = h.hexdigest()[5]
            if not index.isnumeric() or int(index) > 7:
                continue
            if password[int(h.hexdigest()[5])] is None:
                password[int(h.hexdigest()[5])] = h.hexdigest()[6]
            print('Password (so far): %s' % (''.join([x or '_' for x in password])))

    print('password: %s' % (password, ))


if __name__ == '__main__':
    main()
