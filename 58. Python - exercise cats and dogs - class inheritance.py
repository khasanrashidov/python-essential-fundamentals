## exercise: cats and dogs - class inheritance

print('#' * 50, '\n')

class Pet(object):
    def __init__(self, name):
        self.name = name
        print(self.name)

class Dog(Pet):
    def __init__(self, name):
        super().__init__(name)

    def speak(self):
        print('Woof!')

class Cat(Pet):
    def __init__(self, name):
        super().__init__(name)

    def speak(self):
        print('Meow!')


fish = Pet('Nemo')

print()

dog = Dog('Rex')
dog.speak()

print()

cat = Cat('Tom')
cat.speak()

print('\n' + '#' * 50 + '\n')

##################################################
