# Write a program to check whether a triangle is valid or not, when the three angles of the triangle are entered through the keyboard. A triangle is valid if the sum of all the three angles is equal to 180 degress.

angle1 = int(input('Enter the first angle of the triangle: '))
angle2 = int(input('Enter the second angle of the triangle: '))
angle3 = int(input('Enter the third angle of the triangle: '))

sum = angle1 + angle2 + angle3

if sum==180:
   print('The triangle is valid')
else:
    print('The triangle is not valid') 