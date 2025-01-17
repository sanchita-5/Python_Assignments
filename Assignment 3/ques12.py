# Write a program to add first seven terms of the following series using a for loop: 1/1! + 2/2! + 3/3! + ... + n/n!

sum = 0.0
for i in range(1,8):
    fact = 1.0
    for j in range(1,i+1):
        fact = fact * j
    sum = sum + i/fact
print('Sum of series =',sum)