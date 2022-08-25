time = int(float(input('Enter time : ')))

if    time in range(8, 18):     print('At university')
elif  time in range(18, 23):    print('At home')
elif  time in range(23, 0) or (0, 5):     print('In bed')
elif  time in range(5, 8):      print('Woke up, had a shower and preparing')
else:                           print('Outworld')
##############################

y = 10
x = 1 if (y == 10) else 2
print(x)
x = 3 if (y == 1) else 2 if (y == -1) else 1
print(x)

##############################

z = int(float(input('Enter a number : ')))

res = 'even' if (not(z % 2))  else 'odd'

print(res)

##############################
# checking if the string is in another string

string = 'Hi Python'
if 'Hi' in string:
    print ('There is!')
else:
    print ('There is no!')
    
##############################
a = 3; b = 5; print(a, b)
