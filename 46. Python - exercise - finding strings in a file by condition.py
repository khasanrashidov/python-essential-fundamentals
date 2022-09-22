## exercises
print('#' * 50)
print()

## finding strings in a file by condition

f = open('names.txt', 'r')
## print(f.read()) ## to print all names in the file

##################################################

## to print names starting with particular letter

#### 1st way
##for name in f.readlines():
##    if name[0] == 'S':
##        print(name.strip())

#### 2nd way
## the splitlines() method splits a string into a list
## The startswith() method returns True
## if the string starts with the specified value,
## otherwise False.
for l in f.read().splitlines(): ## f.read().splitlines() is a list now
    if l.startswith('S'):
        print(l)

#### or 3rd way
##for l in f.readlines():
##    if l.startswith('S'):
##        print(l.strip())
        
f.close()

print('\n' + '#' * 50 + '\n')
##################################################
