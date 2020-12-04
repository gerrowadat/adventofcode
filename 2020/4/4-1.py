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