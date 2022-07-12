# Write a program which prompts the user for a Celsius temperature, convert the temperature to Fahrenheit, and print out the converted temperature.

C=float(input('Enter Tempatature in Celsius: '))
F=(C*1.8)+32
print(f'Temparature in Farenheit: {F}')
print('Temparature in Farenheit %.4f'%F)
