def valid_hgt(hgt):
    if 'cm' in hgt:
        hgt_cm = int(hgt.split('c')[0])
        if 150 <= hgt_cm <= 193:
            return True
    if 'in' in hgt:
        hgt_in = int(hgt.split('i')[0])
        if 59 <= hgt_in <= 76:
            return True
    print('invalid hgt %s' % (hgt, ))
    return False

def valid_hcl(hcl):
    if len(hcl) != 7:
        print('invalid hcl %s' % (hcl, ))
        return False
    if hcl[0] != '#':
        print('invalid hcl %s' % (hcl, ))
        return False
    for c in hcl[1:]:
        if c not in '0123456789abcdef':
            print('invalid hcl %s' % (hcl, ))
            return False
    return True
  
# hweh hweh hweh
def parseport(raw):
    """Return True if valid, false if not"""
    fields = {}
    rawfields = raw.split(' ')
    for f in rawfields:
        (k, v) = f.split(':')
        fields[k] = v
    for required in ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']:
      if required not in fields:
          return False
    # byr
    if not 1920 <= int(fields['byr']) <= 2002:
        print('invalid byr %s' % (fields['byr']))
        return False
    if not 2010 <= int(fields['iyr']) <= 2020:
        print('invalid iyr %s' % (fields['iyr']))
        return False
    if not 2020 <= int(fields['eyr']) <= 2030:
        print('invalid eyr %s' % (fields['eyr']))
        return False
    if not valid_hgt(fields['hgt']):
        print('invalid hgt %s' % (fields['hgt']))
        return False
    if not valid_hcl(fields['hcl']):
        print('invalid hcl %s' % (fields['hcl']))
        return False
    if fields['ecl'] not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
        print('invalid ecl %s' % (fields['ecl']))
        return False
    if len(fields['pid']) != 9 or not fields['pid'].isnumeric():
        print('invalid pid %s' % (fields['pid']))
        return False

    return True


def main():
    with open('2020/4/input.txt') as f:
        lines = f.readlines()

    passports = []
    accum = ''
    for l in lines:
        if l == '\n':
            passports.append(accum.strip(' '))
            accum = ''
        else:
            accum += l.replace('\n', ' ')
    # get the last one.
    passports.append(accum.strip(' '))

    valid_count = 0
    for p in passports:
        valid = parseport(p)
        if valid:
            valid_count += 1
        print ('PASS %s: %s' % (valid,p))
    print ('%d valid passports' % (valid_count, ))

main()