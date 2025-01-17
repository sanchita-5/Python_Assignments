# Given the lenth and breadth of a rectangle, write a program to find whether the area of the rectangle is greater than its perimeter. For example, the area of the rectangle with lenth = 5 and breadth = 4 is greater than its perimeter.

l = int(int(input('Enter the length of rectangle: ')))
b = int(input('Enter the breadth of rectangle: '))
area = l*b
peri = 2*(l+b)
if area>peri:
    print('Area is greater than perimeter')
else:
    print('Area is not greater than perimeter')