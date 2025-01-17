# Two numbers are entered through the keyboard. Write a program to find the value of one number raised to the power of another.

x = float(input('Enter first number: '))
y = int(input('Enter second number: '))
power = i = 1
while i<=y:
    power = power*x
    i = i+1
print(x, 'to the power', y, 'is', power)
#print(x**y)