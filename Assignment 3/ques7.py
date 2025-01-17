# Write a program to enter the numbers till the user wants and at the end it should display the count of positive, negative and zeros entered.

pos = neg = zero = 0
choice = 1
while choice > 0:
    num = int(input('Enter the number: '))
    if num == 0:
        zero += 1
    elif num < 0:
        neg += 1
    elif num > 0:
        pos += 1

    choice = int(input('Do you want to enter another number? (Enter 1 for yes & 0 for no): '))
print('Zeroes =',zero)
print('Negatives =',neg)
print('Positive =',pos)