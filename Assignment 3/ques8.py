# Write a program to find the octal equivalent of the entered number.

decimal_num = int(input('Enter a decimal number: '))
octal_num = ''
while decimal_num > 0:
    r = decimal_num % 8
    octal_num = str(r) + octal_num
    decimal_num //= 8
print('The octal equivalent is:', octal_num)