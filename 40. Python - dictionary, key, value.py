## dictionary - unordered collection
print('#' * 50)
print()

## creation
##
## empty dictionary
d = {}

## 'list' cannot be a key of 'dictionary'

## instances of classes can be keys of dictionary,
## provided that they support certain methods
## which inform the interpreter that they deal with
## immutable object.

## literal
## keys should be unique and immutable
## e.g. numbers, strings, tuples
## values can be in any type of object
d = {1: 1, 2: 'two', (1,2):[1,2]}
print(d)

## function dict
d = dict(dog = 'cобака',  cat = ['кот', 'кошка'])
d1 = dict([(1, 'one'), (2, 'two')])
print(d, d1, sep = '\n')

## dictionary generator
d = {a:  a ** 2 for a in range(7)}; print(d)

## the output can be unordered
d = {'a' : 1, 'b' : 2, 'c' : 3}; print(d)

print('\n' + '#' * 50 + '\n')

##################################################

## accessing the key
d = {1: 1, 'two': 2, (1,2):[1,2]} 

print(d['two'])
print(d.get('some_key', 'no such key'))

## adding an element
d['five'] = 5
print(d)

## deleting the element (key) using del()
## del(dict_name['key_name']
del(d['five'])
print(d)

## getting the keys
print(d.keys())
## getting the values
print(d.values())

print('\n' + '#' * 50 + '\n')

##################################################

def get_choice(k):
    d = {1: 'yes',
         2: 'no',
         3: 'I do not know'}
    return d.get(k, 'You do not know what you want')

#ch = int(input('Your choice is '))
ch = 5
print(get_choice(ch))

print('\n' + '#' * 50 + '\n')

##################################################

def calculator(x, action):
    f2 = lambda x: x + 2
    f3 = lambda x: x + 3
    d = {'add_2': f2(x), 'add_3': f3(x)}
    return(d[action])

print(calculator(2, 'add_2'))
print(calculator(2, 'add_3'))

