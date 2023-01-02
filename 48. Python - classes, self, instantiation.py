## classes

print('#' * 50)
print()

## Constructors are generally used for instantiating an object.
## The task of constructors is to initialize(assign values)
## to the data members of the class when an object of the class is created.
## In Python the __init__() method is called the constructor
## and is always called when an object is created.

## Types of constructors : 
##
## default constructor:
## The default constructor is a simple constructor
## which doesn’t accept any arguments.
## Its definition has only one argument
## which is a reference to the instance being constructed.
##
## parameterized constructor:
## constructor with parameters is known as parameterized constructor.
## The parameterized constructor takes its first argument
## as a reference to the instance being constructed known as self
## and the rest of the arguments are provided by the programmer.

## '__init__', '__str__' are magical methods
## Magic methods in Python are the special methods
## that start and end with the double underscores.

class Coordinate(object):
    ## self, and other variables,
    ## if those variables are not assigned then they have default values
    def __init__(self, x = 0, y = 0):  ## parametrized constructor
        self.x = x
        self.y = y
    ## We need to remember that __init__ method
    ## requires parameters while creating the object
    ## otherwise it gives an error.
    
## instantiation
## Instantiating a class is creating a copy of the class
## which inherits all class variables and methods.
## Instantiating a class in Python is simple.
## To instantiate a class,
## we simply call the class as if it were a function,
## passing the arguments that the __init__ method defines.
## The return value will be the newly created object.

a = Coordinate(1, 2)
b = Coordinate(3, 4)

## print(variable_name.attribute_name)

print(a.x, a.y, b.x, b.y)

zero = Coordinate()
print(zero.x, zero.y)

print()
print('#' * 50)
print()
##################################################
