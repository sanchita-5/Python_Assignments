# If the three sides of a triangle are entered through the keyboard, write a program to check whether the triangle is valid or not. The triangle is valid if the sum of two sides is greater than the largest of the three sides.

side1 = int(input('Enter first side of triangle: '))
side2 = int(input('Enter second side of triangle: '))
side3 = int(input('Enter third side of triangle: '))

if side1>side2:
    if side1>side3:
        sum = side2+side3
        largeside = side1
    else:
        sum = side1+side2
        largeside = side3
else:
    if side2>side3:
        sum = side1+side3
        largeside = side2
    else:
        sum = side1+side2
        largeside = side3
if sum>largeside:
    print('The triangle is valid')
else:
    print('The triangle is an invalid triangle')