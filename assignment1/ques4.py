# Temperature of a city in Farenheit degrees is input through the keyboard. Write a program  to convert this temperature into Centigrade degrees.

f = float(input('Enter the temperature in Farenheit: '))
c = (f-32)*5/9
print('Temperature in celcius = ',c)