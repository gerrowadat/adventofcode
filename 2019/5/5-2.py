#!/usr/bin/python

import sys


class IntCodeOperation(object):
  def __init__(self, opcode):
    self._opcode = opcode[-2:]
    if len(self._opcode) == 1:
      self._opcode = '0' + self._opcode
    self._posmodes = [0,0,0]
    self._params = []

    if len(opcode) >= 3:
      self._posmodes[0] = int(opcode[-3])
    if len(opcode) >= 4:
      self._posmodes[1] = int(opcode[-4])
    if len(opcode) >= 5:
      self._posmodes[2] = int(opcode[-5])

  def __str__(self):
    return 'opcode [%s] params %s  param_modes %s' % (self.opcode, self.params, self._posmodes)

  @property
  def opcode(self):
    return self._opcode

  @property
  def params(self):
    return self._params

  def param_mode(self, param_idx):
    return self._posmodes[param_idx]

  def set_params(self, params):
    self._params = params
    

  
class IntCodeComputer(object):
  OPCODES = {
    '99': ('Halt', 0),
    '01': ('Add', 3),
    '02': ('Multiply', 3),
    '03': ('Input', 1),
    '04': ('Output', 1),
    '05': ('JumpIfTrue', 2),
    '06': ('JumpIfFalse', 2),
    '07': ('LessThan', 3),
    '08': ('Equals', 3)
  }

  def __init__(self, program):
    self._cursor = 0
    self._p = program.split(',')

  def Store(self, pos, val):
    print('store: [%s] -> %s (was %s)' % (pos, val, self._p[int(pos)]))
    self._p[int(pos)] = str(val)

  def ConsumeOp(self):
    """Consume Op, and then forward control point to beyond its parameters."""
    opcode = self._p[self._cursor]
    self._cursor += 1

    op = IntCodeOperation(opcode)
    (method_name, param_count) = self.OPCODES[op.opcode]
    op.set_params(self._p[self._cursor:self._cursor+param_count])
    print('%s' % (op, ))
    self._cursor += param_count

    method = getattr(self, '_%s' % (method_name, ))

    return method(op)

  def _GetParam(self, op, idx):
    mode = op.param_mode(idx)
    if mode == 0:
      return self._p[int(op.params[idx])]
    return op.params[idx]

  def _Add(self, op):
    first = self._GetParam(op, 0)
    second = self._GetParam(op, 1)

    result = int(first) + int(second)

    print('add %s, %s: %s' % (first, second, str(result)))

    self.Store(op.params[2], str(result))
    return True

  def _Multiply(self, op):
    first = self._GetParam(op, 0)
    second = self._GetParam(op, 1)

    result = int(first) * int(second)

    print('mult %s, %s: %s' % (first, second, str(result)))

    self.Store(op.params[2], str(result))
    return True

  def _Input(self, op):
    inp = input('Input: ')
    self.Store(op.params[0], inp)
    return True

  def _Output(self, op):
    out = self._GetParam(op, 0)
    print('> : %s' % (out, ))
    return True

  def _JumpIfTrue(self, op):
    val = self._GetParam(op, 0)
    if int(val) != 0:
      print('true: jump to %d' % (int(self._GetParam(op, 1))))
      self._cursor = int(self._GetParam(op, 1))
    else:
      print ('false: resume')
    return True

  def _JumpIfFalse(self, op):
    val = self._GetParam(op, 0)
    if int(val) == 0:
      print('false: jump to %d' % (int(self._GetParam(op, 1))))
      self._cursor = int(self._GetParam(op, 1))
    else:
      print ('true: resume')
    return True

  def _LessThan(self, op):
    print('lt %s, %s' % (int(self._GetParam(op, 0)), int(self._GetParam(op, 1))))
    store_pos = int(op.params[2])
    if int(self._GetParam(op, 0)) < int(self._GetParam(op, 1)):
      self.Store(store_pos, '1')
    else:
      self.Store(store_pos, '0')
    return True

  def _Equals(self, op):
    print('eq %s, %s' % (int(self._GetParam(op, 0)), int(self._GetParam(op, 1))))
    store_pos = int(op.params[2])
    if int(self._GetParam(op, 0)) == int(self._GetParam(op, 1)):
      self.Store(store_pos, '1')
    else:
      self.Store(store_pos, '0')
    return True

  def _Halt(self, op):
    print('halt')
    return False

  def Process(self):
    while True:
      success = self.ConsumeOp()
      if not success:
        break

with open(sys.argv[1]) as f:
  program = f.readline().strip('\n')

c = IntCodeComputer(program)

c.Process()
