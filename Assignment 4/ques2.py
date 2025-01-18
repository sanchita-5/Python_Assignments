# Write a program in Python to check if a given number is even or odd using the function.

def evodd(num):
    if num%2==0:
        print("The number is even")
    else:
        print("The number is odd")

num=int(input("Enter a number to check if it is even or odd: "))
evodd(num)