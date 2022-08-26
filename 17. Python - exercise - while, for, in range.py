print('#' * 50)
print()
num1 = 1
while num1 <= 100:
    print(num1)
    num1 += 1
print()
##################################################
print('#' * 50)
print()
for num2 in range(1, 101):
    print(num2)
print()
##################################################
## printing multiples of n
print('#' * 50)
print()
import random
n = random.randint (0, 100)
##n = 67
##n = 3
for i in range(0, 101):
    if not(i % n):
        print(i)
print()
##################################################
## another solution for the code above
print('#' * 50)
print()
n = random.randint(1, 100)

# Code here:
for i in range(0, 101, n):
    print(i)
print()
