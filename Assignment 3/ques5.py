# Write a program to print out all the Armstrong numbers between 1 and 500. If sum of cubes of each digit of the number is equal to the number itself, then the number is called an Armstrong number. For example, 153 = (1*1*1) + (5*5*5) + (3*3*3)

for num in range(1, 501):
    original_num = num
    sum_of_cubes = 0
    
    while num > 0:
        digit = num % 10
        sum_of_cubes += digit ** 3
        num //= 10

    if original_num == sum_of_cubes:
        print(original_num)

