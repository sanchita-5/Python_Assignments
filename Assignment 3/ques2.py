# Write a program to find the factorial value of any number entered through the keyboard.

num = int(input('Enter a number: '))
fact = i = 1
while i<=num:
    fact = fact*i
    i = i+1
print('Factorial value of',num, '=',fact)