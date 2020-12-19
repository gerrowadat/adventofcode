import re

def addfirst_calc(expr):
  add_re = r'\b(\d+?)\b\s+\+\s+\b(\d+?)\b'
  m = re.search(add_re, expr)
  while m:
    result = int(m.group(1)) + int(m.group(2))
    add_replace = r'\b%s\b' % m.group(0).replace('+', '\+')
    expr = re.sub(add_replace, str(result), expr)
    m = re.search(add_re, expr)

  mult_re = r'\b(\d+?)\b\s+\*\s+\b(\d+?)\b'
  m = re.search(mult_re, expr)
  while m:
    result = int(m.group(1)) * int(m.group(2))
    mult_replace = r'\b%s\b' % m.group(0).replace('*', '\*')
    expr = re.sub(mult_replace, str(result), expr)
    m = re.search(mult_re, expr)

  return int(expr)

def main():
  with open('input.txt') as f:
    raw = f.readlines()

  total = 0

  for line in raw:
    line = line.strip('\n')
    paren_re = r'\(([^()]+)\)'
    m = re.search(paren_re, line)
    while m:
      result = addfirst_calc(m.group(0)[1:-1])
      line = line.replace(m.group(0), str(result))
      m = re.search(paren_re, line)

    result = int(addfirst_calc(line))
    total += result

  print ('Total: %d' % (total, ))
      
main()
