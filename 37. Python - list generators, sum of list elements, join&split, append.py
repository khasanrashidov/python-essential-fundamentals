## List comprehensions and generators
print('#' * 50)
print()

## list generator
lst = [i ** 3 for i in range(10)]
print(lst)
print()

lst = [i ** 3 for i in range(10) if i != 5]
print(lst)
print()

## generator with condition
lst = [i**3 for i in range(10) if (i**3) % 2]
print(lst)

## sum of list elements using generator
res = sum([i**3 for i in range(10) if (i**3) % 2])
print(res)

## matrix
lst = [[i * j for i in range(1, 5)] for j in range(1, 5)]
for item in lst: print(item)
print(lst[1][1])

## multiplication table
lst = [[ i * j for i in range(1, 10)] for j in range(1, 10)]
for item in lst: print(item)

print()

print('3 times 4 is', lst[2][3])
## or
print('4 times 3 is', lst[3][2])

print()
print('#' * 50)
print()
##################################################

## join and split methods

mail = 'khasan_rashidov@mail.ru'
print(mail)

lst = mail.split('@')
print(lst)
## If there is no parameter (argument) in split() method,
## then the list is split by space as the default split is space.

s = '\'at\''.join(lst)
print(s)
## If there is empty string ('') applied with join method,
## then then elements of the list will just be joined altogether
## as a whole single string.

lst = mail.split('a')
print(lst)

s = 'a'.join(lst)
print(s)

## In this cases we can convert string to list
## and do some transformations with the list
## and then convert the list to string back again.

##################################################

## We need to note that lists are mutable, therefore
## list methods, as against string methods, change the list itself,
## and therefore there is no need to reassign
## the result of method operation. 

lst0 = []
for i in range(10):
    lst0.append(i)
print(lst0)

##################################################

lst1 = []
## forming a list from 10 to 2 with step (difference) of 1 (or -1)
for i in range(10, 1, -1): 
    lst1.append(i)
    
print(lst1)

print('#' * 50)
print()
##################################################
