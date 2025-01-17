# A five-digit number is entered through the keyboard. Write a program to obtain the reversed number and to determine whether the original and reversed numers are equal or not.

num = int(input('Enter a five digit number: '))
e = num%10
d = (num//10)%10
c = (num//100)%10
b = (num//1000)%10
a = (num//10000)

#reversing the number
x = e*10000 + d*1000 + c*100 + b*10 +a
print('The reverse number is: ',x)
if x==num:
    print('Reverse and Original number are equal')
else:
    print('Reverse and original number are not equal')