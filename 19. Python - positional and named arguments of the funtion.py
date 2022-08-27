## positional and named arguments of funtion
print('#' * 50)
print()
def person_info(first_name = 'No first name', \
                last_name = 'No last name', \
                country = 'No country', \
                city = 'No city'):
    print('First name :', first_name)
    print('Last name :', last_name)
    print('Country :', country)
    print('City :', city)
    print('_' * 50, '\n')
    
## positional arguments - order matters
person_info('Khasan','Rashidov','Uzbekistan','Karshi')

## named arguments 
person_info(city = 'London', last_name = 'Rush',
            first_name = 'Harry', country = 'Great Britain')

## for default values
person_info()
##################################################
