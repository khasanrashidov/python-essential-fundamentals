## exercise - creating classes, methods and its instances

print('#' * 50, '\n')

class Person(object):
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

p = Person('Khasan', 'Rashidov')
print(p.first_name, p.last_name)

print('\n' + '#' * 50 + '\n')
##################################################
