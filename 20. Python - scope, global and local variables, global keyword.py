separator = '#' * 50
print(separator)
print()

def f1():
    x = 'local_1'
    print(x)

def f2():
    x = 'local_2'
    print(x)

x = 'global_var_x'
f1()
f2()
print(x)

print()

##################################################

print(separator)
print()

def f1():
    x = 'local_1'
    print(x)

def f2():
    x = 'local_2'
    print(x)
    print(y)
    f1() ## calling a function inside another

x = 'global_var_x'
y = 'global_var_y'
f2()
print(x)

print()

##################################################

print(separator)
print()

def f3():
    global z
    z = 'changed_global_var_z'

z = 'global_var_z'
print(z)
f3()
print(z)

print()

## In Python, global keyword allows to modify the variable
## outside of the current scope.
## It is used to create a global variable
## and make changes to the variable in a local context.

