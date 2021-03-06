#!/usr/bin/python

import sys

class Object(object):
  def __init__(self, name, parent=None):
    self._name = name
    self._parent = parent

  def __str__(self):
    return '%s (parent: %s)' % (self.name, self.parent)

  @property
  def name(self):
    return self._name

  @property
  def parent(self):
    return self._parent

class StarMap(object):
  def __init__(self):
    self._objects = []

  @property
  def objects(self):
    return self._objects

  def add_object(self, obj):
    existing = self.get_object(obj.name)
    if existing:
      if obj.parent and not existing.parent:
        existing.parent = obj.parent
        return
    else:
      self._objects.append(obj)
    
  def get_object(self, name):
    ret = [x for x in self._objects if x.name == name]
    if ret:
      return ret[0]
    return None

  def steps_to_com(self, name):
    o = self.get_object(name)
    if o is None:
      raise ValueError('no such object %s' % (name, ))

    print('orbits for %s' % (o, ))

    steps = []
    while o.name != 'COM':
      steps.append(o)
      o = self.get_object(o.parent)
      if o is None:
        raise ValueError('no parent for %s' % (steps[-1].name, ))

    print('steps: %s' % ([x.name for x in steps]))

    return steps


with open(sys.argv[1]) as f:
  lines = f.readlines()

orbits = []

for l in lines:
  orbits.append((l.strip('\n').split(')')))

m = StarMap()

m.add_object(Object('COM', None))

for orbit in orbits:
  o = Object(orbit[1], orbit[0])
  m.add_object(o)
  print(o)

print('%s total objects' % (len(m.objects)))

you_orbiting = m.get_object(m.get_object('YOU').parent)
san_orbiting = m.get_object(m.get_object('SAN').parent)

you_steps = m.steps_to_com(you_orbiting.name)
san_steps = m.steps_to_com(san_orbiting.name)

print('YOU->COM: %s' % ([x.name for x in you_steps]))
print('SAN->COM: %s' % ([x.name for x in san_steps]))

found = False

for you_idx in range(0, len(you_steps)):
  for san_idx in range(0, len(san_steps)):
    if you_steps[you_idx].name == san_steps[san_idx].name:
      
      print('Distance: %d (via %s)' % ((you_idx + san_idx), you_steps[you_idx].name))
      found = True
      break
  if found:
    break
