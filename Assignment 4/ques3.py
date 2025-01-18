# Write a program in Python to calculate sum of Fibonacci series.
n = int(input("Enter the number of terms: "))
a = 0
b = 1
sum_fib = 0
for i in range(n):
    sum_fib += a 
    temp = a+b 
    a = b
    b = temp
print('The sum of the Fibonacci series is:',sum_fib)