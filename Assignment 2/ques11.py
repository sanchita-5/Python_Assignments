# Given the coordinates (x, y) of a center of a circle and it's radius, write a program which will determine whether a point lies inside the circle, on the circle or outside the circle. (Hint: Use sqrt() and pow() functions)

import math
x = float(input('Enter the x coordinate of center: '))
y = float(input('Enter the y coordinate of center: '))
r = float(input('Enter the radius of circle: '))

x1 = float(input('Enter the value of x1 coordinate of point: '))
y1 = float(input('Enter the value of y1 coordinate of point: '))

d = math.sqrt(pow((x-x1),2.0) + pow((y-y1),2.0))
if d<r:
    print('Point is inside the circle')
elif d==r:
    print('Point is on the circle')
elif d>r:
    print('Point is outside the circle')