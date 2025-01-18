def hcf(x,y):
    while y:
        x,y=y,x%y
    return x

num1=int(input("Enter the first number: "))
num2=int(input("Enter the second number: "))
HCF=hcf(num1,num2)
print("hcf of two number: ",HCF)