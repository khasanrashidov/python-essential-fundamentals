## classes, methods

print('#' * 50, '\n')

from random import choice as c

def info():
    print('A new hamster is born!')

class Hamster(object):
    def __init__(self, color):
        self.color = color
        info() ## calling the function which is outside the class
        print('Color -', self.color)

    def breed(self, other):
        new_color = c(
            (self.color, other.color,
             '{} and {}'.format(self.color, other.color)))
        return Hamster(new_color)

mikki = Hamster('white')
catty = Hamster('black')
mica = mikki.breed(catty)

print('\n' + '#' * 50 + '\n')
##################################################
