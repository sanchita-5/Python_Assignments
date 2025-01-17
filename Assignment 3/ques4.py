# Write a program to print all the ASCII values and their equivalent characters using a while loop. The ASCII values vary from 0 to 255 [chr(110) will print ascii character of the value 110. ord('A') will print corresponding ASCII value of 'A']

ascii_value = 0
while ascii_value <= 255:
    character = chr(ascii_value)
    print(ascii_value, character)
    ascii_value += 1