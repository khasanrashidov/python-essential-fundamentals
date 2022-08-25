## ternary operator
print()
x=33
print('yes') if x==33 else print('no') if x>33 \
             else print('maybe')
x=30
print('yes') if x==33 else print('no') if x>33 \
             else print('maybe')
x=36
print('yes') if x==33 else print('no') if x>33 \
             else print('maybe')

print('='*30)
## program to check whether a number is even or odd
y=5
if y%2==0:
    print(y, 'is even')
else:
    print(y, 'is odd')
## or we can use ternary operator
print(y, 'is even') if y%2==0 else print(y, 'is odd')

## another way (the same ternary operator)

msg='is even' if y%2==0 else 'is odd'
print(y, msg)
