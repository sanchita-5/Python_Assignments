# If the ages of Ram, Shyam and Ajay are input through the keyboard, write a program to determine the youngest of the three. 

age1 = int(input('Enter age of Ram: '))
age2 = int(input('Enter age of Shyam: '))
age3 = int(input('Enter age of Ajay: '))

if age1<age2:
    if age1<age3:
        print('Ram is Youngest')
    else:
        print('Ajay is Youngest')

else:
    if age2<age3:                               
        print('Shyam is Youngest')
    else: 
        print('Ajay is Youngest')

'''
if age2<age1:
    if age2<age3:                               
        print('Shyam is Youngest')
    else: 
        print('Ajay is Youngest')

'''

#if age2<age3:
#    if age2<age1:
#       print('Shyam is Youngest')
#    else: 
#        print('Ram is Youngest')

#if age1==age2==age3:
 #   print('Everybody is of same age')
