# Write a program to print all prime numbers from 1 to 300. (Hint: Use nested loops, break and continue)

print('Prime numbers between 1 and 300 are:')
for n in range(2,301):
    is_prime = True
    for i in range(2,n):
        if n % i == 0:
            is_prime = False
            break
        
    if is_prime:
        print(n,end = ' ')