import re

def ltr_calc(expr):
  print('TOT: %s' % (expr, ))
  words = expr.split(' ')
  total = 0
  instr = 'plus'
  for f in words:
    if f == '+':
      instr = 'plus'
      continue
    if f == '*':
      instr = 'mult'
      continue
    # We assume a number at this point yay
    num = int(f)
    if instr == 'plus':
      print('%d + %d == %d' % (total, num, total + num))
      total += num
      continue
    if instr == 'mult':
      print('%d * %d == %d' % (total, num, total * num))
      total = total * num
  return total

def main():
  with open('input.txt') as f:
    raw = f.readlines()

  total = 0

  for line in raw:
    line = line.strip('\n')
    # Substitute inner parens until no more parens.
    paren_re = r'\(([^()]+)\)'
    m = re.search(paren_re, line)
    while m:
      result = ltr_calc(m.group(0)[1:-1])
      line = line.replace(m.group(0), str(result))
      print(line)
      m = re.search(paren_re, line)

    total += ltr_calc(line)

  print ('Total: %d' % (total, ))
      
main()
