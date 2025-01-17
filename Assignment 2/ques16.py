# If the three sides of a triangle are entered through the keyboard, write a program to check whether the traiangle is isosceles, equilateral, scalene or right angled triangle.

x=int(input('Enter the value of first side: '))
y=int(input('Enter the value of second side: '))
z=int(input('Enter the value of third side: '))

if x*x+y*y==z*z:
    print ('The triangle is right angle')
elif x==y and y==z:
    print('The triangle is equilateral')
elif x==y and x!=z or y==z and y!=x or x==z and x!=y :
    print('The triangle is isosceles')
else:
    print('The triangle is scalene')