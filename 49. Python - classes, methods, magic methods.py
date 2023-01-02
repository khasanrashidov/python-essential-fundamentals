## classes, methods

print('#' * 50)
print()

## '__init__', '__str__' are magical methods
## Magic methods in Python are the special methods
## that start and end with the double underscores.

class Coordinate(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    ## method distance for class Coordinate
    ## self is the reference to the object, to which the method is applied
    ## other is an arbitrary argument
    def distance(self, other):
        x_dist = (self.x - other.x) ** 2
        y_dist = (self.y - other.y) ** 2
        return (x_dist + y_dist) ** 0.5
    ## distance = ((x2 − x1) ** 2 + (y2 − y1) ** 2) ** 0.5

    def __str__(self):
        return '{}, {}'.format(self.x, self.y)

home = Coordinate(0, 0)
shop = Coordinate(3, 4)

## print(object1.method(object2))
print('distance:', home.distance(shop))
print()

## It is necessary to use method __str__ to print the object
## parameters properly; without method __str__ ,
## only the address will be printed.
print(home) 
print(shop)

print()
print('#' * 50)
print()
##################################################
