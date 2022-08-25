print()
a = 14

if a >= 10:
    print('111')
else:
    print('000')
if a > 20:
    print('000')
else:
    print('111')
if a % 7 != 0:
    print('000')
else:
    print('111')

##############################

import random
a = random.randint(0, 130)
print(a)
if a in range(18, 124):
    print('Hello')
elif a in range(0, 18):
    print('Goodbye')
elif a not in range(0, 123):
    print('Error')

##############################
import random
a = random.randint(0, 130)

if a >= 0 and a < 18:
  print("Goodbye")
elif a >= 18 and a <= 123:
  print("Hello")
else:
  print("Error")
##############################

import random
num = random.randint(0, 100)
print(num)

num = num**2 if num > 10 else num**3 if num <= 10 else None

## or
## print(a**2) if a > 10 else print(a**3)
print(num)
