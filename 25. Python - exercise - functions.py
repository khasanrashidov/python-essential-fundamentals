print()

def add2(a, b):
    sum2 = a + b
    return sum2

def add3(a, b, c):
    sum3 = a + b + c
    return sum3

## or just
##def add2(a, b):
##    return a+b
##    
##def add3(a, b, c):
##    return a+b+c


import random as r
from random import randint as rint

a = rint(1, 100)
print('a =', a)
b = rint(1, 100)
print('b =', b)
c = rint(1, 100)
print('c =', c)

print('a + b =', add2(a, b))
print('a + b + c =', add3(a, b, c))

print('\n', '#' * 50, '\n')

##################################################

## program to find the biggest among three numbers
## using ternary operator
## in real life it is enough to use just
## built in function max() :)

def get_biggest(num1, num2, num3):
    biggest3 = num1 if num1 > num2 and num1 > num3 \
    else num2 if num2 > num1 and num2 > num3 else num3
    return biggest3
num1 = int(float(input('Enter 1st number : ')))
num2 = int(float(input('Enter 2nd number : ')))
num3 = int(float(input('Enter 3rd number : ')))

max3 = get_biggest(num1, num2, num3)
print()
print('The biggest number among', '|', num1, '|', num2, '|', num3, '|', \
      'is', max3)

print('\n', '#' * 50, '\n')

##################################################

def double(number):
    return 2 * number

number = int(float(input(('Enter a number : '))))
twice = double(number)
print('Twice of', number, 'is', twice)

print('\n', '#' * 50, '\n')

##################################################

def hello(name = 'World'):
    return print('Hello', name)
hello()
hello('Harry')
## this program outputs 'Hello World'
## if the function is called without arguments, hello()

print('\n', '#' * 50, '\n')

##################################################

f = lambda a, b : a * b
print(f(6, 4))
print(f(10, -2))

print('\n', '#' * 50, '\n')

##################################################

def factorial(num):
    if num == 1 or num == 0:
        return 1
    else:
        return (num * factorial(num - 1))
    
num = int(float(input('Enter an integer number : ')))
fact = factorial(num)
print('Factorial of', num, 'is', fact)

print('\n', '#' * 50, '\n')

## or just
## def factorial(n):
##  if n == 0:
##    return 1
##  return n * factorial(n - 1)
