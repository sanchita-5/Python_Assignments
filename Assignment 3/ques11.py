# Write a program to fill the entire screen with a smiling face. The smiling face has an ASCII value 1.

for r in range(0,25):
    for c in range(0,80):
        print(chr(1),end = " ")