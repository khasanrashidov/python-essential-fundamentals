print('#' * 50)
print()
def net_salary(gross_salary, income_tax):
    '''
    gross_salary: positive number int of float
    income_tax: rate of income tax, decimal, 10% = 0.1
    returns net_salary, rounded to 2 digits
    '''
    print('Gross salary :', gross_salary)
    rate = 1 - income_tax
    return round(gross_salary * rate, 2)

net_sal = net_salary(1000, 0.13)
print('Net salary :', net_sal)
print()

## If there is no return in the function,
## but it is still called, then the function
## will just return None.
##
## The return should be in the end of the defined function,
## because the return acts like the break in the function,
## and everything after return will not be executed.

##################################################

def greeting(name):
    pass ## don't forget to complete
## pass is a null statement,
## it is used in functions, loops and classes
## The interpreter does not ignore a pass statement,
## but nothing happens
## and the statement results into no operation.
## The pass statement is useful
## when we don't write the implementation of a function
## but we want to implement it in the future.

##################################################
