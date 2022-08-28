## Lambda functions
## syntax: 
## lambda arguments : expression

print('#' * 50)
print()
## A lambda function is a small anonymous function.
## A lambda function can take any number of arguments,
## but can only have one expression.
def f(a, b):
    return a + b
f1 = lambda a, b: a + b
print(f(1, 2))
print(f1(1, 2))
print((lambda a, b: a ** b)(2, 3))
print()

##################################################
x = lambda a : a + 10
print(x(5))
##################################################
x = lambda a, b : a * b
print(x(5, 6))
##################################################
x = lambda a, b, c : a + b + c
print(x(5, 6, 2))
##################################################
## It is good to use lambda functions
## when an anonymous function is required
## for a short period of time.
