## list
print()

lst = [3, 4, 5, 1]
print(lst)
print()

for item in lst: print(item, end = ' ')
print()

for i in range (len(lst)):
    print(lst[i], end = ' ')
print()

print()

lst1 = lst[0:-1:2] ## start, stop (end), step
print(lst1)
print()

lst2 = lst[::2]
print(lst2)
print()

lst3 = lst[:] ## entire copy of the list
print(lst3)

print('\n', '#' * 50, '\n')
##################################################
## We need to note that we don't have a concept of arrays in python.
## Arrays can be created using, for example, lists.
## 2D array using list
lst = [[1, 2, 3],
       [3, 3, 1],
       [2, 5, 1]]
print(lst)
print()

print(lst[2][1]) ## 2Dlist[row][column]
