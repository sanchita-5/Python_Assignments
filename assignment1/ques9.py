# If a four-digit number is input through the keyboard, write a program to obtain the sum of the first and last digit of this number. 

n = int(input('Enter a four digit number: '))

d4 = n%10   #4th digit
n = n//10    #remaining digits
d3 = n%10   #3rd digit
n = n//10    #remaining digit
d2 = n%10   #2nd digit
n = n//10    #remaining digits
d1 = n%10   #1st digit

sum = d4 +d1
print('The sum of the first and the last entered digits is ',sum)