## coin flipping

import random

from random import randint

counter_0 = counter_1 = 0

print()

for i in range(100):
    if randint(0, 1) == 0:
        counter_0 += 1
    else:
        counter_1 +=1

print('Heads:', counter_0)
print('Tails:', counter_1)

print()
