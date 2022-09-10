## dictionaries
## getting the key by its value

print('#' * 50)
print()

d = {'one' : 1, 'two' : 2, 'three' : 3, 3 : 3}

## k is key, v is value
## two k and v should be in for loop to traverse in dictionary
for k, v in d.items():
    if v == 3:
        print(k)
        print('key of', v, '-', k)

print('#' * 50)
print()
##################################################

n = int(input('Enter a number : '))

if n == 1:
    print('one')
elif n == 2:
    print('two')
else:
    print('I don\'t know such number')

print('#' * 50)
print()

## the above program can be written using dictionaries
n1 = int(input('Enter a number : '))
d1 = {1 : 'one', 2 : 'two'}
print(d1.get(n1, 'I don\'t know such number'))

print('#' * 50)
print()
##################################################

## sorting the dictionary

d2 = {'c' : 'three', 'a' : 'one', 'b' : 'two'}
print(d2)
print()

## sorted() returns values in
## increasing order (numbers)
## or in alphabetical orders (string)
for key in sorted(d2.keys()):
    print(key, d2[key])

print()
print(d2)

print()
print(sorted(d2.keys()))

print()
print(sorted(d2.values()))

print()
print(sorted(d2.items()))

print()
voc = (sorted(d2.items())).copy() ## we may omit .copy() here
print(voc)

print('#' * 50)
print()

##################################################

## sorting the dictionary by its keys
d = {a:  a ** 2 for a in range(7)}
print(d)
print('Sorted dictionary')
for k in sorted(d.keys()):
    print(k, d[k])

print('#' * 50)
print()

##################################################

## saving ordered dictionary
## import of the module must be done in the beginning

from collections import OrderedDict
d1 = OrderedDict(sorted(d.items()))
print(d1)
