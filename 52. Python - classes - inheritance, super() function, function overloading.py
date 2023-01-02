## classes - inheritance, super() function

print('#' * 50, '\n')

class Ship(object):
    def __init__(self, speed):
        '''
        'speed' is in knots.
        A knot is a unit of speed
        equal to one nautical mile per hour.
        In other words, it is about 1.8 km/h.
        '''
        self.speed = speed

    def move(self, time):
        '''
        'time' is in hours
        '''
        dist = self.speed * time
        print('{} miles traveled'.format(dist))

    def __str__(self):
        return 'speed: {}'.format(self.speed)

class Submarine(Ship):
    ## Important moment, if parent class has __init__ method,
    ## then all child classes should have __init__ method as well.
    def __init__(self, speed, position = 1):
        '''
        If position is 1, then submarine is above water,
        else if it is 0 then submarine is underwater.
        '''
        ## initializing the attributes of parent class
        ## is implemented using function 'super()';
        ## The super() function returns intermediary object
        ## which delegates in parent method calls.
        ## But in class definition we can use super() without parameters.
        ## Syntax: super().init(attributes)
        super().__init__(speed)
        self.position = position
        if self.position:
            print('Submarine is above water.')
        else:
            print('Submarine is underwater.')

    ## By default, move() method works fine
    ## with instances of Submarine class (child class) as well.
    ## But, in addition, we can redefine or
    ## overload parent methods in child classes.
    def move(self):
        if self.position:
            print('The submarine began to dive.')
        else:
            print('The submarine surfaced.')

cruiser = Ship(20)
cruiser.move(2)
print('Cruiser\'s', cruiser)

print()

aurora = Submarine(40, 0)
aurora.move()
print('Aurora\'s', aurora)

## In python, it is possible to create a class
## directly based on several classes,
## it is called a multiple inheritance.

print('\n' + '#' * 50 + '\n')
##################################################
