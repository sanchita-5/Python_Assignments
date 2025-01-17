# Ramesh's basic salary is input through the keyboard. His dearness allowance is 40% of basic salary, and house rent allowance is 20% of basic salary. Write a program to calculate his gross salary.

bp = float(input('Enter Basic Salary of Ramesh: '))
da = 0.4*bp
hra = 0.2*bp
grpay = bp + da + hra
print('Basic Salary of Ramesh = ',bp)
print('Dearness Allowance = ',da)
print('House Rent Allowance = ',hra)
print('Gross Pay of Ramesh is ',grpay)