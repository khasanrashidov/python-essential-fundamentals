import random

# This will return a list of 4 numbers selected from the range 0 to 40, without duplicates.
num1, num2, num3, num4 = random.sample(range(0, 41), 4)  # in range 0 <= x < 41

print("randomnum1 =", num1)
print("randomnum2 =", num2)
print("randomnum3 =", num3)
print("randomnum4 =", num4)
