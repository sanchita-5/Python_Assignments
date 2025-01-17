# A cashier has currency notes of denominations 10, 50 and 100. If the amount to be withdrawn is input through the keyboard in hundreds, find the total number of currency notes of each denomintion the cashier will have to give to the withdrawer.

amount=int(input('Enter the amount to be withdrawn: '))
nohun=amount//100
amount=amount%100
nofifty=amount//50
amount=amount%50
noten=amount//10
amount=amount%10

print('No. of hundreds: ',nohun)
print('No. of fifties: ',nofifty)
print('No. of tens: ',noten)
