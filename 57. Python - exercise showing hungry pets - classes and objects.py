## exercise: showing hungry pets - classes and objects

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
        self.hunger = new_hunger
        
    def __str__(self):
        msg = self.name
        if self.hunger >= 80:
            msg += ' is hungry.'
        else:
            msg += ' is not hungry or just was fed.'
        return msg

cat = Pet('Tom')
print(cat)

print()

cat.feed(30)
print(cat)


print('\n' + '#' * 50 + '\n')
##################################################
