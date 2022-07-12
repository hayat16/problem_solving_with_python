Write a Python program to calculate the area of a trapezoid.

h=float(input('Enter Height : '))
val_1=float(input('Enter base 1 value :'))
val_2=float(input(' Enter base 2 value : '))
area=((val_1+val_2)*h)/2
print(f'Area : {area}')
print('Area %.4f'%area)
