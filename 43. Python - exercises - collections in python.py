## exercises
print('#' * 50)
print()

## creating new string

def underlined(string):
    return '{}\n{}'.format(string, '_' * len(string))

## or
##
##def underlined(string):
##    print(string)
##    print('_' * len(string))

string = input('Enter the string : ')
print()
print(underlined(string))

print()
print('#' * 50)
print()
##################################################

## vowel or consonant

VOWELS = 'aeiouy'
CONSONANTS = 'bcdfghjklmnpqrstvwxz'
ALPHABET = 'abcdefghijklmnopqrstuvwxyz'

for letter in ALPHABET:
    if letter in VOWELS:
        print(letter + ' vowel')
    elif letter in CONSONANTS:
        print(letter + ' consonant')

print()
print('#' * 50)
print()
##################################################

## reverse the string

def reverse_string(s):
    return '{}'.format(s[::-1])
    ## or just
    ## return s[::-1]

s = input('Enter the string : ')
print('Reversed string :', reverse_string(s))

print()
print('#' * 50)
print()
##################################################

## obtaining the date from ISO format

str1 = '2022-01-15T05:55'
str2 = '2022-01-25T09:21'

def get_date(iso_string):
    index = iso_string.find('T')
    iso_string = iso_string[0 : index]
    return iso_string
    ## or just
    ## return iso_string[:iso_string.find('T')]

print(get_date(str1))
print(get_date(str2))

print()
print('#' * 50)
print()
##################################################

## printing the number of occurrences of each symbol in string

my_string = input('Enter the string : ')

#### version of solution which outputs the char which occurred once as well
##def print_count(my_string):
##    for character in my_string:
##        counted = my_string.count(character, 0, len(my_string))
##        print(character, counted)  
##
## version of solution which doesn't output the char which occurred before
def print_count(my_string):
    counted = ''
    for character in my_string:
        if character not in counted:
            print('{} {}'.format(character, my_string.count(character)))
            counted += character

print(print_count(my_string))

print()
print('#' * 50)
print()
##################################################

## program that makes one sorted and merged tuple of two tuples
## all elements are type of string

def sorted_merged(tuple1, tuple2):
    return sorted(tuple1 + tuple2)

## for input
##
## taking user input, it takes input as string
## (numbers will be of string type)

t1 = ()
t2 = ()

n1 = int(float(input('Enter number of elements for tuple 1 : ')))
for number in range(0, n1):
    element1 = input()
    t1 += (element1, )
print(t1)

print()

n2 = int(float(input('Enter number of elements for tuple 2 : ')))
for number in range(0, n2):
    element1 = input()
    t2 += (element1, )
print(t2)

print()
print('Sorted and merged tuple :', sorted_merged(t1, t2))

print()
print('#' * 50)
print()

##################################################

## common elements in tuple

def commonElements(tuple1, tuple2):
    return_tuple = tuple()
    for element in tuple1:
        if element in tuple2:
            return_tuple += (element, )
        else: continue ## we can omit this line, it will work fine as well
    return return_tuple


t1 = 5, 3, 2, 'a', 'z', 7.7
t2 = 2, 'a', 4, 5

print('Common elements :', commonElements(t1, t2))

print()
print('#' * 50)
print()
##################################################

## set of divisors

def divisors(n):
    set_divisors = {i for i in range (1, n + 1) if n % i == 0}
    return set_divisors

n = int(float(input('Enter the number : ')))
print('Divisors of', n, ':', divisors(n))
print()

divisors_390 = divisors(390)
print('Divisors of 390 :', divisors_390)
print()

divisors_96 = divisors(96)
print('Divisors of 96 :', divisors_96)
print()

common_divisors = divisors_390 & divisors_96
print('Common divisors of 390 and 96 :', common_divisors)

print('\n' + '#' * 50 + '\n')

##################################################

## creating lists

int_list = [10, 20, 30, 30, 10]
print(int_list)
print('size of int_list is', len(int_list))

str_list = ['abc', 'cde', 'fgh', 'ijk', 'lmn']
print(str_list)
print('size of str_list is', len(str_list))

print('\n' + '#' * 50 + '\n')

##################################################

## creating list from square of the numbers in the list

#### using simple function
##def square_list(input_list):
##    return_list = list() ## or: return_list = []
##    for element in input_list[:]:
##        element **= 2
##        return_list.append(element)
##    return return_list

## using list generator
def square_list(input_list):
    return [element ** 2 for element in input_list]

list_a = [3, 2, 6]
list_b = [71, 43, 31, 21, 92, 27, 14, 46, 40, 100]

print(square_list(list_a))
print()

print(square_list(list_b))
print()

print('#' * 50)
print()

##################################################

## adding the element to the beginning of the list
def insert(d, i):
    '''
    function adds (appends) element to the beginning of the list
    not to the end; i is an element of the list d
    '''
    ## using method list.insert(i, x)
    d.insert(0, i)
    return d

print(insert([3, 5, 6], 9))

print('\n' + '#' * 50 + '\n')

##################################################

## creating a dictionary

age = {'Khasan': 20, 'James': 24, 'Hyuna': 23}
print(age)

print('\n' + '#' * 50 + '\n')

##################################################

print(None) ## None
print(type(None)) ## <class 'NoneType'>

print('\n' + '#' * 50 + '\n')

##################################################

## finding max value in dictionary

dict_example = {'a' : 1, 'b' : 2, 'c' : 3, 'f' : 0}

def max_dict(d):  
  max_v = None
  for k, v in d.items():
    if (not max_v) or (v > max_v):
      max_v = v
      ret = k
  return ret

## another solution
##def max_dict(d):
##    max_v = 0
##    for k, v in d.items():
##        if v > max_v:
##            max_v = v
##            ret = k
##    return ret

print('Key of max value in dictionary is', max_dict(dict_example))

print('\n' + '#' * 50 + '\n')

##################################################

## printing names of the students by name in sorted way 

grades = {'Анна': 5, 'Евгения': 3, 'Екатерина': 4, 'Ирина': 3, 'Злата': 2, 'Светлана': 3,
          'Алиса': 4, 'Юрий': 4, 'Нина': 5, 'Татьяна': 4, 'Ульяна': 4, 'Яна': 4, 'Константин': 3,
          'Андрей': 5, 'Тимур': 4, 'Павел': 4, 'Сергей': 3, 'Василий': 4, 'Виктория': 5,
          'Евгений': 4, 'Илья': 5, 'Лев': 4, 'Владислав': 3, 'Максим': 5, 'Люся': 3, 'Денис': 4,
          'Кристина': 3, 'Никита': 4, 'Регина': 3, 'Дарья': 4, 'Диана': 4, 'Оксана': 4}

for key in sorted(grades.keys()):
    print(key, grades[key])

print('\n' + '#' * 50 + '\n')

## printing sorted grades (values of keys)

## printing sorted grades (values of keys)

for k, v in grades.items():
    if v == 5:
        print(k, v)
else:
    for k, v in grades.items():
        if v == 4:
            print(k, v)
    else:
        for k, v in grades.items():
            if v == 3:
                print(k, v)
        else:
            for k, v in grades.items():
                if v == 2:
                    print(k, v)
    
##################################################
