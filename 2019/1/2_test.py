#!usr/bin/python

import math

def fuel_needed(mass):
    fuel = math.floor(mass/3) - 2
    if fuel <= 0:
       return 0
    fuel_for_fuel = fuel_needed(fuel)
    if fuel_for_fuel <= 0:
      return fuel
    return fuel + fuel_for_fuel

answer = fuel_needed(100756)

print('%s\n' % (answer, ))

