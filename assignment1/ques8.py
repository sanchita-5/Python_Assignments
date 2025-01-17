# If a five digit number is input through the keyboard, write a program to reverse the number. 

n = int(input('Enter a five digit number: '))
d5 = n%10   # 5th digit
n = n//10    #remaining digits
d4 = n%10   #4th digit
n = n//10    #remaining digits
d3 = n%10   #3rd digit
n = n//10    #remaining digit
d2 = n%10   #2nd digit
n = n//10    #remaining digits
d1 = n%10   #1st digit
revnum = d5*10000 + d4*1000 + d3*100 + d2*10 +d1
print('The reversed number is ',revnum)