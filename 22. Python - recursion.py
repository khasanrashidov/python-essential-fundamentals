print('#' * 50, '\n')

def hi(n):
    if n == 0:
        return
    else:
        print('Hi')
        print('Recursion')
        print()
    hi(n-1)

hi(3)
print('#' * 50, '\n')
##################################################
'''
Actually, recursion is not universally better design.
Often, calling functions repeatedly like this wastes space
on the stack, and the implementation can be much less efficient.
Our recursive formulation of factorial, for example,
is a terrible design.
'''
