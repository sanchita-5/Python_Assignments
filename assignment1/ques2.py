# The distance between two cities (in km) is input through the keyboard. Write a program to convert and print this distance in meters, feet, inches and centimeters.

km = float(input('Enter the distance in Kilometers: '))
m = km*1000
cm = m*100
inch = cm/2.54
ft = inch/12
print('Distance in meters = ',m)
print('Distance in centimeter = ',cm)
print('Distance in inches = ',inch)
print('Distance in feet = ',ft)