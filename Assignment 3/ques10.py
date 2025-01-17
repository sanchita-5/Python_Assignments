# Write a program to find the range of a set of numbers. Range is the difference between the smallest and biggest number in the list.

n = int(input('Enter how many numbers you want to enter: '))
num = int(input('Enter the number: '))
max = min = num
for i in range(1,n):
    num = int(input('Enter the number: '))
    if num > max:
        max = num
    if num < min:
        min = num
range = max - min
print(range, 'is the range of the data')
