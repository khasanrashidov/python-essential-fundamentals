## string
## Sequenial access to elements 
print()
## checking occurrence
word = 'Python'
letter = 't'

if letter in word:
    print(letter * len(word))
    
## another example
if 'n' in 'hello':
    print('yes')
else:
    print('no')

print()
print('#' * 50)
##################################################

print()

word = 'Python'

for item in word:
    print(item)
    
print()
print('#' * 50)
##################################################

print()
## constants are written in all capital letters
## and
## underscores separating the words

VOWELS = 'eyuioa'
word = 'Python'
new_word = ''

for item in word:
    if item in VOWELS:
        continue
    else:
        new_word += item

print(new_word)

print()
print('#' * 50)
##################################################

## accessing string elements by index
word = 'Python'

print(word[0])
print(word[1])

print()

for i in range(len(word)):
    print('Index:', i, 'Symbol:', word[i])

## slices

new_word = word[0]
print(new_word)

new_word = word[1:5]
print(new_word)

new_word = word[:] ## copy of the string
print(new_word)

new_word = word[0::1] ## copy of the string
print(new_word)

new_word = word [::-1] ## to reverse the string
print(new_word)
