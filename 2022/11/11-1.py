#!/usr/bin/env python

import sys
import math

class Monkey(object):
    def __init__(self):
        self._items = []
        self._operation = None
        self._test_div = 1
        self._true_throw = None
        self._false_throw = None
        self._inspections = 0

    def __str__(self):
        ret = ''
        ret += 'M%s ' % (str(self._items))
        ret += 'OP%s ' % (self._operation)
        ret += 'DIV[%d] %d ? %d ' % (self._test_div, self._true_throw, self._false_throw)
        return ret

    @property
    def items(self):
        return self._items

    @property
    def inspections(self):
        return self._inspections

    def all_thrown(self):
        self._items = []

    def from_spec(self, spec):
        self._items = [int(x) for x in spec[1].split(':')[1].split(',')]
        self._operation = spec[2].split()[-2:]
        self._test_div = int(spec[3].split()[-1])
        self._true_throw = int(spec[4].split()[-1])
        self._false_throw = int(spec[5].split()[-1])

    def _op(self, item):
        (operator, operand) = self._operation
        if operand == 'old':
            operand = item
        if operator == '*':
            return item * int(operand)
        elif operator == '+':
            return item + int(operand)

    def inspect(self, item):
        # Perform operation and return new worry level
        self._inspections += 1
        new_worry =  self._op(item)
        return int(math.floor(new_worry / 3))

    def throw(self, item):
        new_worry = self._op(item)
        new_worry = int(math.floor(new_worry / 3))
        if new_worry % self._test_div == 0:
            return self._true_throw
        else:
            return self._false_throw

    def catch(self, item):
        self._items.append(item)
        

def main():
    filename = sys.argv[1]
    with open(filename) as f:
        lines = f.readlines()

    monkeys = {}

    for m in range(0, len(lines)+1, 7):
        monkey_spec = lines[m:m+7]
        monkey_num = int(monkey_spec[0].strip()[-2])
        m = Monkey()
        m.from_spec(monkey_spec)
        monkeys[monkey_num] = m
        print(monkeys[monkey_num])

    rounds = 20

    for r in range(rounds):
        for m in monkeys:
            for i in monkeys[m].items:
                new_worry = monkeys[m].inspect(i)
                new_m = monkeys[m].throw(i)
                monkeys[new_m].catch(new_worry)
            monkeys[m].all_thrown()


    for m in monkeys:
        print(monkeys[m])

    for m in monkeys:
        print('Monkey %d inspected items %d times.' % (m, monkeys[m].inspections))

    top2 = sorted([x.inspections for x in monkeys.values()])[-2:]

    print('Monkey Business: %d' % (top2[0] * top2[1]))



if __name__ == '__main__':
    main()
