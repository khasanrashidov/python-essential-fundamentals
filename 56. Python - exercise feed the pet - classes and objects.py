## exercise: feed the pet - classes and objects

print('#' * 50, '\n')

from random import randint as rint

class Pet(object):
    def __init__(self, name):
        self.name = name
        self.hunger = rint(0, 100)
        print('hunger:', self.hunger)
        ## If hunger is 0, then it means that the pet was fed.

    def feed(self, points):
        '''
        'points' are points to feed to make the pet hunger equal 0
        '''
        points = max(0, points)
        print('feed points:', points)
        new_hunger = max(0, self.hunger - points)
        print('new hunger:', new_hunger)
        hunger = new_hunger


cat = Pet('Tom')
cat.feed(30)

print('\n' + '#' * 50 + '\n')
##################################################
