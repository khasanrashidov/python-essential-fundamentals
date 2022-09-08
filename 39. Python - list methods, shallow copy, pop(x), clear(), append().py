## List comprehensions and generators
print('#' * 50, '\n')

## We need to note that lists are mutable, therefore
## list methods, as against string methods, change the list itself,
## and therefore there is no need to reassign
## the result of method operation.

lst = [4, 2, 3]
lst.append(1)
print(lst)

lst1 = []
for i in range(10):
    lst1.append(i)

print(lst1)

print('#' * 50, '\n')

##################################################

lst2 = [1, 1, 1]
new_lst = lst2
new_lst.clear()
print(lst2)
## obviously if we print(lst2) the output is just [] (empty list)
## the thing is that assignment operation did not create a new object,
## it created the reference (or link) to that same object,
## and all variables which refer to that object obtained
## new modified value
print('#' * 50, '\n')

##################################################

def get_first_item(input):
    if type(input) == list:
        ## returning the popped element
        return input.pop(0)
        ## in .pop(0) we are
        ## deleting 1st element of the list
        ## at index [0]

lst3 = [100, 0, 5]
print(get_first_item(lst3))
print(lst3)

print('#' * 50, '\n')

##################################################

## shallow copy
## shallow copy can be implemented using two ways:
## 1) using slices: list = list[:]
## 2) using .copy() method: list = list.copy()

lst4 = [1, 1, 1]
new_lst = lst4[:] ## shallow copy of the entire list
new_lst.clear()
print(lst4)

print('#' * 50, '\n')

def get_first_item(input):
    if type(input) == list:
        input = input.copy() ## shallow copy using method .copy()
        ## or we can use
        ## input = input[:]
        return input.pop(0) ## deleting 1st element of the list

lst5 = [100, 0, 5]
print(get_first_item(lst5))
print(lst5)

print('#' * 50, '\n')

## So, when working with lists in python,
## we need to make a shallow copy to work with them.
## It is not hard, it is just one line of code, which
## can save a lot of time and nerves. :)

##################################################
