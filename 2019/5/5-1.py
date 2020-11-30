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
    '04': ('Output', 1)
  }

  def __init__(self, program):
    self._cursor = 0
    self._p = program.split(',')

  def Store(self, pos, val):
    print('store: [%s] -> %s (was %s)' % (pos, val, self._p[int(pos)]))
    self._p[int(pos)] = val

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

  def _GetParam(self, param, mode):
    if mode == 0:
      return self._p[int(param)]
    return param

  def _Add(self, op):
    first = self._GetParam(op.params[0], op.param_mode(0))
    second = self._GetParam(op.params[1], op.param_mode(1))

    result = int(first) + int(second)

    print('add %s, %s: %s' % (first, second, str(result)))

    self.Store(op.params[2], str(result))
    return True

  def _Multiply(self, op):
    first = self._GetParam(op.params[0], op.param_mode(0))
    second = self._GetParam(op.params[1], op.param_mode(1))

    result = int(first) * int(second)

    print('mult %s, %s: %s' % (first, second, str(result)))

    self.Store(op.params[2], str(result))
    return True

  def _Input(self, op):
    inp = input('Input: ')
    self.Store(op.params[0], inp)
    return True

  def _Output(self, op):
    out = self._GetParam(op.params[0], op.param_mode(0))
    print('> : %s' % (out, ))
    return True

  def _Halt(self, op):
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
