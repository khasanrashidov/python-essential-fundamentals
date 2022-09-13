##################################################
## fundamentals of working with files
print('#' * 50)
print()

## We are setting'encoding = 'utf-8'' because
## text file has Cyrillic alphabet/symbols.
## Without utf-8 encoding we cannot open fles
## consisting of Russian letters.
f = open('zen.txt', 'r', encoding = 'utf-8')
## to print entire text
print(f.read())
f.close() ## closing the file

print('\n' + '#' * 50 + '\n')
##################################################

f = open('zen.txt', 'r', encoding = 'utf-8')
## to print (till) first n particular symbols (includingly)
print(f.read(10))
f.close()

print('\n' + '#' * 50 + '\n')
##################################################

f = open('zen.txt', 'r', encoding = 'utf-8')
## a loop which will print every line but with empty line in-between
for line in f:
    print(line)
f.close()

print('\n' + '#' * 50 + '\n')
##################################################

f = open('zen.txt', 'r', encoding = 'utf-8')
## the loop above but printing using the method strip(), which
## deletes empty line (space) from the beginning and the end
for line in f:
    print(line.rstrip()) ## or just without using 'r': line.strip() 

f.close()

print('\n' + '#' * 50 + '\n')
##################################################

## other ways to print the info (or data, or text) from file

f = open('zen.txt', 'r', encoding = 'utf-8')
## f.readline() method prints one line of text with empty (next) line
print(f.readline()) ## '\n'
f.close()

print('\n' + '#' * 50 + '\n')
##################################################

f = open('zen.txt', 'r', encoding = 'utf-8')
## the following method reads every line in text and
## returns the list, the elements of which are
## lines of text with next line symbol
print(f.readlines())
f.close()

print('\n' + '#' * 50 + '\n')
##################################################

f = open('zen.txt', 'r', encoding = 'utf-8')
lines = f.readlines()
print(lines[5])
f.close()

print('\n' + '#' * 50 + '\n')
##################################################
