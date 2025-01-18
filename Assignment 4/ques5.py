def hcf(x,y):
    while y:
        x,y=y,x%y
    return x


num1=int(input("Enter the first number: "))
num2=int(input("Enter the second number: "))
HCF=hcf(num1,num2)
LCM=num1*num2//HCF
print("lcm of two number: ",LCM)