# Write a program in python to find the square of any number using the function.

def square(x):
    y = x*x
    return y
def main():
    a = float(input('Enter any number: '))
    b = square(a)
    print('Square of',a,'is',b)
if __name__ == '__main__':
    main()
