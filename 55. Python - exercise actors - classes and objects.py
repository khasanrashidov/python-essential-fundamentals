## exercise: actors - classes and objects

print('#' * 50, '\n')

class Person(object):
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

actor_names = [
    {'first_name': "Jack",    'last_name': "Nicholson"},
    {'first_name': "Marlon",  'last_name': "Brando"},
    {'first_name': "Robert",  'last_name': "De Niro"},
    {'first_name': "Al",      'last_name': "Pacino"},
    {'first_name': "Daniel",  'last_name': "Day-Lewis"},
    {'first_name': "Dustin",  'last_name': "Hoffman"},
    {'first_name': "Tom",     'last_name': "Hanks"},
    {'first_name': "Anthony", 'last_name': "Hopkins"},
    {'first_name': "Paul",    'last_name': "Newman"},
    {'first_name': "Denzel",  'last_name': "Washington"},
]

for actors in actor_names:
    ## printing the values of the dictionary
    ## in the element of the list
    print(actors['first_name'], actors['last_name'])

    ## creating an object using values of the dictionary
    a = Person(actors['first_name'], actors['last_name'])

    ## printing the first name and the last name
    ## via class objects
    print(a.first_name, a.last_name)

## another way to do this, is using list comprehensions   
## actors = [Person(a['first_name'], a['last_name']) for a in actor_names]

print('\n' + '#' * 50 + '\n')
##################################################
