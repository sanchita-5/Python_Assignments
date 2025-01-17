# Given a point(x, y), write a program to find out if it lies on the x-axis, y-axis or at the origin, viz(0,0).

x = float(input('Enter x coordinate: '))
y = float(input('Enter y coordinate: '))

if x==0 and y==0:
    print('The point is on the origin')
if x==0 and y!=0:
    print('The point lie on the y axis')
if x!=0 and y==0:
    print('The point lie on the x axis')
if x!=0 and y!=0:
    print('The point lie on the plane')
