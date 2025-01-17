# An Insurance company follows following rules to calculate premium.
# If a person's health is excellent and the person is between 25 and 35 years of age and lives in a city and is a male then the premium is Rs. 4 per thousand and his policy amount cannot exceed Rs. 2 lakhs.
# If a person satisfies all the above conditions except that the sex is female then the premium is Rs. 3 per thousand and her policy amount cannot exceed Rs. 1 lakh.
# If a person's health is poor and the person is between 25 and 35 years of age and lives in a village and is a male then the premium is Rs. 6 per thousand and his policy cannot exceed Rs. 10,000.
# In all other cases the person is not insured.
# Write a program to output whether the person should be insured or not, his/her premium rate and maximum amount for which he/she can be insured.

health=int(input('Enter your health condition(exc=1,poor=0): '))
age=int(input('Enter your age: '))
residance=int(input('Enter your residance place(city=1,village=0): '))
gender=input('Enter your gender(m,f): ')

if health==1 and age>=25 and age<=35 and residance==1 and gender=='m':
    print('Premium is Rs. 4 per thousand and your policy amount cannot exceed Rs. 2 lakhs!')
elif health==1 and (age>=25 and age<=35) and residance==1 and gender=='f':
    print('Premium is Rs. 3 per thousand and your policy amount cannot exceed Rs. 1 lakh!')
elif health==0 and (age>=25 and age<=35) and residance==0 and gender=='m':
    print('Premium is Rs. 6 per thousand and your policy amount cannot exceed Rs. 10000!')
else:
    print('You are not insured!!')