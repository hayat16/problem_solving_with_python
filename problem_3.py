# Write a program which prompts the user for the height and width of a rectangle, calculate the area, diagonal, and perimeter.

import math
height=float(input('Enter Height: '))
width=float(input('Enter Width: '))
area=height*width
Perimeter=2*(height+width)
Diagonal=2*math.sqrt(pow(height,2)+pow(width,2))
print(f'Area : {area}')
print(f'Perimete : {Perimeter}')
print(f'Diagonal : {Diagonal}')
print('Diagonal : %.4f'%Diagonal)
