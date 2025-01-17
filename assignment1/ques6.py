# Two numbers are input through the keyboard into two locations C and D. Write a program to interchange the contents of C and D.

C = int(input('Enter the first number: '))
D = int(input('Enter the second number: '))
temp = C
C = D 
D = temp
print('After interchange:')
print('C =',C)
print('D =',D)