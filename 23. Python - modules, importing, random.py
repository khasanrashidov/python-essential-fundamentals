print()
import random as r
from random import randrange, choice
## from random import * ## it is not recommended at all

## random.randint(x, y) - (x <= n <= y)
number = r.randint(1, 10)
print(number)

## random.randrange(start, stop, step)
number1 = randrange(1, 101, 2)
print(number1)

## random.choice(sequence)
mylist = [1, 2, 3]
print(choice(mylist))

## random.random() - random number between 0 and 1
print((round(r.random())))

for i in range(10):
    print(r.random())

print()
print('#' * 50)
##################################################
