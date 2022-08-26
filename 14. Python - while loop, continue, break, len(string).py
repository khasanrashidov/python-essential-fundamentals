print()

##while True:
##    user_name = input('Add username >>> ')
##    ## len(string) - length of the string
##    if len(user_name) >= 5:
##        if user_name == 'admin':
##            print('Enter other name')
##            continue ## continue - returns the control to the beginning of the while loop
##        else:
##            print('User is added :', user_name)
##            break ## break - exits the loop
##    print('Username length should be at least 5 characters! \
##\nTry again!\n')
##print('_' * 50, '\n The loop is ended')
    
##############################

print('_' * 50)
print()
n = 4 ## counter
while n >= 1 :
    user_name = input('Add username >>> ')
    ## len(string) - length of the string
    if len(user_name) >= 5:
        if user_name == 'admin':
            print('Enter other name')
            continue ## continue - returns the control to the beginning of the while loop
        else:
            print('User is added :', user_name)
            break ## break - exits the loop
    n -=1
    print('Username length should be at least 5 characters! \
\nTry again!\nATTEMPTS LEFT :', n, '\n')
    if n == 0:
        print('YOU GOT NO ATTEMPTS LEFT, RUN THE PROGRAM AGAIN')
    
print('_' * 50, '\nThe loop has finished')
