print()
print('=======  Multiplication table  =======')
for i in range(1, 11):
    for j in range(1, 11):
        res = str(i * j)
        print (res, end=' ' * (4 - len(res)))
##    if i == 2:
##        break
    print()
else: 
    print('======  Loop worked completely. ======')
    print('======  Loop ended naturally.   ======')
## we use 'else:' with 'for loop' or 'while loop'
## to check if the loop ended naturally
