def execute(program, flip=None):
  """  program (list): program listing
       flip (int): Flip the nth jmp/nop encountered
       returns (terminates (bool), acc)."""
  acc = 0
  ptr = 0
  visited = []
  jmpnops_seen = 0

  while ptr not in visited:
    if ptr >= len(program):
      return (True, acc)

    visited.append(ptr)

    (i, val) = program[ptr].split()

    # Flip this instruction between jmp and nop
    # If it's the nth such instruction we've encountered
    if i in ('jmp', 'nop'):
      if jmpnops_seen == flip:
        print('Flipping instruction at line %d: %s %s' % (ptr, i, val))
        if i == 'nop':
          i = 'jmp'
        elif i == 'jmp':
          i = 'nop'
      jmpnops_seen += 1

    print('[%d] %s %s' % (ptr, i, val ))
    if i == 'nop':
      ptr += 1
      continue
    if i == 'acc':
      acc += int(val)
      ptr += 1
      continue
    if i == 'jmp':
      ptr += int(val)
      continue

  # We only get here if there's a loop
  return(False, acc)


with open("input.txt") as f:
  lines = [x.strip('\n') for x in f.readlines()]

acc = 0

stack = []

# See if there's a loop
(terminated, acc) = execute(lines)

# Flip instructons as we encounter them and see if we fix things.
flip = 0
while not terminated:
  print('Trying swap of instruction %d encountered' % (flip, ))
  (terminated, acc) = execute(lines, flip=flip)
  flip += 1


print ('Flipping instruction <%d> encountered fixed it. acc = %d' % (flip, acc))
