Write a Python program to calculate arc length of an angle and sector area of a circle.
       Enter Radius: 5
       Enter Angle:  60
       Arc Length: ??
       Sector Area:  ??
       
import math
r=float(input('Enter radius in radians : '))
a=float(input('Enter angle in radians : '))
s=r*a
area=pow(r,2)*(a/2)
print(f' Arc Length: {s}')
print(f' Sector Area: {area}')
