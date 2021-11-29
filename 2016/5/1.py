#!/usr/bin/env python3

import hashlib

def main():
    door = 'ugkcyxxp'
    password = ''

    inc = 0
    while True:
        h = hashlib.md5()
        text = '%s%d' % (door, inc)
        b = text.encode('utf-8')
        h.update(b)
        if h.hexdigest().startswith('00000'):
            print ('digit: %s' % (h.hexdigest()[5]))
            password += h.hexdigest()[5]
            if len(password) == 8:
                break
        inc += 1

    print('password: %s' % (password, ))


if __name__ == '__main__':
    main()
