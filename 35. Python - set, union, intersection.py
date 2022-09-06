## set

## list cannot be an element of the set
print('#' * 50)
print()

a = 'aaaa'
a = set(a)  ## remove duplicates
print(a)

s1 = {1, 2}
s2 = {1, 3}

s3 = s1 | s2 ## union
print(s3)

s4 = s1 & s2 ## intersection
print(s4)


print('#' * 50)
print()
##################################################
