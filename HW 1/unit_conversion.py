#Tess Porter
#tcp46
#CS 171 (lab 070)
print('Welcome to the length conversion wizard.')
print('This program can convert between any of the following lengths.')
print('inches\nfeet\nyards\nmiles\nleagues\ncentimeters\ndecimeters\nmeters\ndecameters\nhectometers\nkilometers')
print('Note: You must use the units exactly as spelled above.\n')
c_factors = {
  'centimeters': 1,
  'inches': 2.54, #inches to cm
  'feet': 30.48, #feet to inches to cm
  'yards': 91.44, #yards to feet to inches to cm
  'miles': 160934.4, #miles to yards to feet to inches to cm
  'leagues': 482803.2, #leagues to yards to feet to inches to cm
  'meters': 100,  #meters to cm
  'decimeters': 10, #decimeters to cm
  'decameters': 1000, #decameters to meters to centimeters
  'hectometers': 10000,
  'kilometers': 100000
}
value = float(input('Enter value:\n'))
from_units = input('Enter from units:\n')
to_units = input('Enter to units:\n')
#Below is the conversion from the original units to the new units
new_val = value * (c_factors[from_units]/c_factors[to_units])
print(value, from_units,'is',round(new_val,4),to_units)