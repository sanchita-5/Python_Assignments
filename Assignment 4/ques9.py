# Write a program in Python to calculate Power(a,b) using function.

def power(x,y):
    p=1
    for i in range(1,y+1):
        p=p*x
    return p
def main():
    x = float(input('Enter 1st number: '))
    y = int(input('Enter 2nd number: '))
    pow = power(x,y)
    print(x, 'to the power', y, '=', pow)
if __name__ == '__main__':
    main()