#!/usr/bin/env python3

def find_all(text, ch):
    idx = 0
    while True:
        f = text.find(ch, idx+1)
        if f == -1: return
        yield f
        idx = f


def split_hns(addr):
    # must....not...regex....
    # We assume there aren't any nested [] in addresses.
    all_op = sorted(find_all(addr, '['))
    all_cl = sorted(find_all(addr, ']'))

    hns = []
    text = []

    text.append(addr[:all_op[0]])
    text.append(addr[all_cl[-1]+1:])

    for i in range(len(all_op)):
        # Add this HNS
        hns.append(addr[all_op[i]+1:all_cl[i]])
        # Capture the text between this closing [] and next opening one.
        if i < len(all_op) -1:
            text.append(addr[all_cl[i]+1:all_op[i+1]])

    return text, hns

def has_abba(addr):
    for i in range(len(addr)-3):
        if addr[i] == addr[i+3] and addr[i+1] == addr[i+2] and addr[i] != addr[i+1]:
            return True
    return False


def main():
    with open('input.txt') as f:
        lines = f.readlines()

    tls_ips = 0

    for l in [x.strip() for x in lines]:
        text, hns = split_hns(l)
        if len([x for x in text if has_abba(x)]) > 0 and len([x for x in hns if has_abba(x)]) == 0:
            print('YES %s : %s %s' % (l, text, hns))
            tls_ips += 1
        else:
            print('NO %s : %s %s' % (l, text, hns))

    print ('TLS IPs: %d' % (tls_ips, ))


if __name__ == '__main__':
    main()
