# Method 1
- num = int(input("Enter a number: "))
fact = 1

if num < 0:
    print("Factorial does not exist")
elif num == 0:
    print("Factorial is 1")
else:
    for i in range(1, num + 1):
        fact *= i
    print("Factorial =", fact)


# Method 2- using math.factorial()

import math

num = int(input("Enter a number: "))
print("Factorial =", math.factorial(num))









