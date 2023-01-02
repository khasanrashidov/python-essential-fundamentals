## classes, methods, static methods

print('#' * 50)
print()

## Static methods in Python are extremely similar to
## python class level methods, the difference being that
## a static method is bound to a class
## rather than the objects for that class.
## This means that a static method can be called
## without an object for that class.

## decorators (@)
## decorator is a command, which allows to change
## the behaviour of the method or function.
from random import choice as c

def info():
    print('A new hamster is born!')

class Hamster(object):
    total = 0 ## class attribute

    @staticmethod ## decorator for static method
    def status(): ## There is no 'self' attribute in static method,
                  ## it is because the static method
                  ## is applied to the whole class, not to the object.
                  ## Therefore, there is no need to pass the reference
                  ## to the object, and parameter 'self' makes no sense here.
                  ## Of course, static methods can have other parameters,
                  ## but in this method there is no need for 'self'.
        print('Total number of hamsters -', Hamster.total)

    def __init__(self, color):
        self.color = color
        ## To access the class attribute it is necessary
        ## to use dot operator in the following way:
        ## Class_name.attribute_name
        ## or using class objects outside the class.
        Hamster.total += 1
        info()
        print('Color -', self.color)

    def breed(self, other):
        new_color = c(
            (self.color, other.color,
             '{} and {}'.format(self.color, other.color))
            )
        return Hamster(new_color)

mikki = Hamster('white')
catty = Hamster('black')
mica = mikki.breed(catty)

## to access the attribute of the class - class_name.attribute_name
##print('Total number of hamsters -', Hamster.total)
print()

## There is NO need of objects to access static methods.
Hamster.status()

print()
print('#' * 50)
print()
##################################################
