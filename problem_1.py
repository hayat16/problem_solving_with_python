# Write a program to prompt the user for hours and rate per hour to compute gross pay.

hour=int(input('Enter hours '))
rate=float(input('Enter rate '))
print(type(hour))
print(type(rate))
print(f'Pay {hour*rate}')
