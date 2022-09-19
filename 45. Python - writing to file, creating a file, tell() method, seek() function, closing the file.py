## writing to file
print('#' * 50)
print()

## opening the file, if file doesn't exist, the program creates new one
## must have exactly one of create/read/write/append mode
f = open('numbers.txt', 'w+')

## write() argument must be str
for i in range(11):
    ##f.write(str(i))
    ## writes number 012345678910 in file,
    ## because the range is 11, in our case.
    ## If we print the statement above, then program will print
    ## the number of written chars (symbols) after each loop
    print(f.write(str(i)))

## After file write() the cursor is in the end of file.

print()
## tell() method returns current position of file object.
## This method takes no parameters and returns an integer value.
## Initially file pointer (cursor) points to the beginning of the file
## (if it is not opened in append mode).
## So, the initial value of tell() is zero.
##
## here in our case, the pointer is in the end
print(f.tell()) 
print()

## seek() function is used to change the position
## of the File Handle to a given specific position.
## File handle is like a cursor,
## which defines from where the data
## has to be read or written in the file.
print(f.seek(0)) ## the cursor is now in the beginning
print()

## now we can read the file (data inside of it), because
## the cursor is in the beginning
print(f.read())
print()

f.close() ## closing the file

print('\n', + '#' * 50 + '\n')

##################################################
