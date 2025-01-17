# According to the Gregorian calendar, it was Monday on the date 01/01/1900. If any year is input through the keyboard write a program to find out what is the day on 1st january of this year.

year = int(input("Enter a year: "))
base_year = 1900
total_days = 0
for y in range(base_year, year):
    if (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0):
        total_days += 366
    else:
        total_days += 365
     
firstday=total_days%7

if firstday==0:    
    print('Monday')
elif firstday==1:    
    print('Tuesday')
elif firstday==2:    
    print('Wednesday')
elif firstday==3:   
    print('Thursday')
elif firstday==4:    
    print('Friday')
elif firstday==5:    
    print('Saturday')
elif firstday==6:    
    print('Sunday')

