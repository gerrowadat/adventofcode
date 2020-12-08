with open("input.txt") as f:
  lines = f.readlines()

acc = 0
ptr = 0
visited_lines = []

while ptr not in visited_lines:
  (i, val) = lines[ptr].strip('\n').split()
  print('[%d] %s' % (ptr, lines[ptr].strip('\n')))
  if i == 'nop':
    visited_lines.append(ptr)
    ptr += 1
    continue
  if i == 'acc':
    visited_lines.append(ptr)
    acc += int(val)
    ptr += 1
    continue
  if i == 'jmp':
    visited_lines.append(ptr)
    ptr += int(val)
    continue

print ('Instruction <%s> at line %d repeated. acc = %d' % (lines[ptr].strip('\n'), ptr, acc))
