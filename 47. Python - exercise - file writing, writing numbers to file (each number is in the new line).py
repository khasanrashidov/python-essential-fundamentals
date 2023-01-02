## exercises
print('#' * 50)
print()

## writing numbers to file (each number is in the new line)
f = open('numbers1k.txt', 'w')

for number in range(1, 1001):
    ## the writing is printed just to see what happens
    ## each loop we can see number of symbols which were written at a time (loop)
    ## it will start from 1 and there will be 1, 2, 3, 4 symbols at each loop
    ## write() argument must be str, not int
    print(f.write(str(number))) 
    ## empty line will take 1 symbol
    print(f.write('\n'))

f.close()

print('\n' + '#' * 50 + '\n')
##################################################
