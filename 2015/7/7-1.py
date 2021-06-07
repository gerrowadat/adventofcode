import sys
import enum
import numpy

class GateType(enum.Enum):
    SIGNAL = enum.auto()
    AND = enum.auto()
    OR = enum.auto()
    NOT = enum.auto()
    LSHIFT = enum.auto()
    RSHIFT = enum.auto()


class Gate(object):
    def __init__(self, spec):
        self._spec = spec
        self._type = None
        self._output = spec.split(' -> ')[1]
        self._operands = []
        self._resolved = False

        spec_parts = spec.split(' -> ')[0].split(' ')
        if len(spec_parts) == 1:
            # direct assignment i.e. 100 -> a
            self._type = GateType.SIGNAL
            self._operands.append(spec_parts[0])
        elif len(spec_parts) == 2:
            # NOT a
            if spec_parts[0] != 'NOT':
                raise ValueError('expecting NOT, got %s' % (spec_parts[0], ))
            self._type = GateType.NOT
            self._operands.append(spec_parts[1])
        else:
            if spec_parts[1] not in GateType.__members__:
                raise ValueError('unknown operator %s' % (spec_parts[1], ))
            self._type = GateType[spec_parts[1]]
            self._operands.append(spec_parts[0])
            self._operands.append(spec_parts[2])

    @property
    def output(self):
        return self._output

    def Resolve(self, vals):
        # return (a, <val>) if a value is resolved, otherwise None.
        # vals are existing known values.

        # See if all operands resolve to tiehter a known value or an int literal.
        resolved_operands = []
        for o in self._operands:
            if o.isnumeric():
                resolved_operands.append(numpy.uint16(o))
            elif o in vals:
                resolved_operands.append(numpy.uint16(vals[o]))

        if len(resolved_operands) != len(self._operands):
            return None
                
        if self._type == GateType.SIGNAL:
            return resolved_operands[0]
        elif self._type == GateType.NOT:
            return self._not(resolved_operands[0])
        elif self._type == GateType.AND:
            return self._and(*resolved_operands)
        elif self._type == GateType.OR:
            return self._or(*resolved_operands)
        elif self._type == GateType.LSHIFT:
            return self._lshift(*resolved_operands)
        elif self._type == GateType.RSHIFT:
            return self._rshift(*resolved_operands)

    def _not(self, val):
        return ~ val

    def _and(self, a, b):
        return a & b

    def _or(self, a, b):
        return a | b

    def _lshift(self, a, bits):
        return a << bits

    def _rshift(self, a, bits):
        return a >> bits


class Circuit(object):
    def __init__(self):
        self._vals = {}
        self._gates = []


    def Load(self, specs):
        for s in specs:
            self._gates.append(Gate(s))

    def Resolve(self):
        unresolved = [g for g in self._gates if g.output not in self._vals]
        while unresolved:
            #print('%d unresolved gates' % (len(unresolved)))
            for g in unresolved:
                ret = g.Resolve(self._vals)
                if ret is not None:
                    print('%s: %s' % (g.output, ret))
                    self._vals[g.output] = ret
            unresolved = [g for g in self._gates if g.output not in self._vals]

    def get_all(self):
        return self._vals

    def get(self, name):
        return self._vals[name]


def main():
    with open(sys.argv[1]) as f:
        lines = [x.strip() for x in f.readlines()]

    c = Circuit()
    c.Load(lines)
    c.Resolve()


if __name__ == '__main__':
    main()
