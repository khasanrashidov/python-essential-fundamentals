## list sorting, adding elements, adding lists
## 
## list0.append(element)
## sorted(list0)
## list1.extend(list2)

## We need to note that lists are mutable, therefore
## list methods, as against string methods, change the list itself,
## and therefore there is no need to reassign
## the result of method operation. 

print('#' * 50)
print()
lst1 = []

# number of elements as input
n1 = int(input("Enter number of elements for list 1 : "))
 
# iterating till the range
for i in range(0, n1):
    element1 = int(float(input()))
    lst1.append(element1) # adding the element to lst1

print()
print('List 1 :', lst1)
lst1 = sorted(lst1) ## sorting the lst1
print()
print('Sorted list 1 :', lst1)
print()

lst2 = []
n2 = int(input("Enter number of elements for list 2 : "))

for i in range (0, n2):
    element2 = int(float(input()))
    lst2.append(element2)

print()
print('List 2 :', lst2)
lst2 = sorted(lst2) ## sorting the lst2
print()
print('Sorted list 2 :', lst2)
print()

lst1.extend(lst2) ## adding lst2 elements to lst1
lst3 = lst1[:] ## copying the lst1 entirely to new lst3
## or just we can use lst3 = lst1, but it does not copy the lst1
lst3 = print('Sorted list 3 (which is list 1 + list 2 elements) :\n', \
      sorted(lst3))
print('#' * 50)
##################################################
