# Write a program to prompt the user for hours and rate per hour to compute gross pay.
# However, the employee who worked above 40 hours give them 1.5 times the hourly rate for individual hours.

#        Enter Hours: 45
#        Enter Rate: 10
#        Pay: 475.0

h=float(input('Enter Hours: '))
r=float(input('Enter Rate: '))
rate=r*1.5
if(h>40):
  d=h-40
  pay=(40*r)+(d*rate)
  print('pay: ',pay)
else:
  pay=h*r
  print('pay : ',pay)
