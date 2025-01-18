# Write a program in Python to calculate factorial of a natural number.

def fact(num):
    factorial = 1
    for i in range(1,num+1):
        factorial = factorial * i
    return factorial
def main():
    num = int(input('Enter a number: '))
    factorial = fact(num)
    print('Factorial of',num, '=', factorial)
if __name__ == '__main__':
    main()
