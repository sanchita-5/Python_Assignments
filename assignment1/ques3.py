# If the marks obtained by a student in five different subjects are input through the keyboard, find out the aggregate marks and percentage marks obtained by the student. Assume that the maximum marks that can be obtained by the student in each subject is 100.

sub1 = int(input('Enter the marks of sub1: '))
sub2 = int(input('Enter the marks of sub2: '))
sub3 = int(input('Enter the marks of sub3: '))
sub4 = int(input('Enter the marks of sub4: '))
sub5 = int(input('Enter the marks of sub5: '))

aggr = sub1 + sub2 + sub3 + sub4 + sub5
per = aggr/5

print('Aggregate Marks = ',aggr)
print('Percentage Marks = ',per)

