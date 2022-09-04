## string
print()
first = 'Khasan'
last = 'Rashidov'
## {} {} without parameters (indices) - positional formation
s = 'Hello, {} {}. Have a nice day!'.format(first, last)
print(s)
s = 'Hello, {1} {0}. Have a nice day, {0}!'.format(first, last)
print(s)
## the {} {} - space between them matters
s = 'Hello, {name}. Have a nice day!'.format(name = 'Harry Rush')
print(s)
s = 'Hello, {name:>10}. Have a nice day!'.format(name = 'Harry')
print(s)
s = 'Hello, {name:^10}. Have a nice day!'.format(name = 'Harry')
print(s)
s = 'Hello, {:<10}. Have a nice day!'.format(first)
print(s)
## {name:10} to set (put) the string in the 10 char space
## 
## {name:>10} to align the string to the right
## {name:<10} to align the string to the left
## {name:^10} to align the string to the center (center align text)
s = 'Hello, {name:*^10}. Have a nice day!'.format(name = 'Harry')
print(s)
## {name:*^10} to fill empty spaces with *
## and by default it is filled by spaces
s = 'Hello, {0:*^10}. Have a nice day!'.format(first)
print(s)
## it is not necessary to indicate the name if the variable in braces 
## so we can just use indexing
w = 10
s = 'Hello, {0:*^{1}}. Have a nice day!'.format(first, w)
print(s)
s = '{:10.3f}'.format(3)
print(s)
## here s = '{:10.3f}'.format(3),
## there is no index that is why just : is written
## length is 10,
## precision is 3, it is 3 symbols after floating point
## f i type of float
## then the number itself in format(3)
print()
print('#' * 50)
##################################################
## for more info for string format method check PEP3101
