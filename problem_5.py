# Write a Python program to calculate surface volume and area of a cylinder.

import math
h=float(input('  Enter Height: '))
r=float(input('  Enter radius: '))
p=math.pi
volume=p*pow(r,2)*h
area=(2*p*r*h)+(2*p*pow(r,2))
print(f'Volume: {volume} & Area {area}')
print('Volume: {:.4f} & Area {:.4f}'.format(volume,area))
