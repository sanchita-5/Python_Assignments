# If a five digit number is input through the keyboard, write a program to calculate the sum of its digits.(Hint: Use the modulus operator '%')

n = int(input('Enter a five digit number: '))
d5 = n%10   # 5th digit
n = n//10    #remaining digits
d4 = n%10   #4th digit
n = n//10    #remaining digits
d3 = n%10   #3rd digit
n = n//10    #remaining digit
d2 = n%10   #2nd digit
n = n//10    #remaining digits
d1 = n%10 
print('The sum of the digits of the number is ',d5+d4+d3+d2+d1)