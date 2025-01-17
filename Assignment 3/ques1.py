# Write a program to calculate overtime pay of 10 employees. Overtime is paid at the rate of Rs. 12.00 per hour for every hour worked above 40 hours. Assume that employees do not work for fractional part of an hour.

i = 1
while i<=10:        # Loop for 10 employees
    hour = int(input('Enter no. of hours worked: '))
    if hour>=40:
        otpay = float((hour-40)*12)
    else:
        otpay = 0
    print('Hours = ', hour, 'Overtime pay = Rs.', otpay)
    i = i+1
