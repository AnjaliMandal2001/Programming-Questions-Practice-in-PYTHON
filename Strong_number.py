'''
A Strong Number is a number whose sum of the factorial of its digits is equal to the original number.
example:
  123= 1! + 2! + 3! = 1+2+6 =9   [not a strong number]
  145= 1! + 4! + 5! = 1+24+120 = 145    [strong number]
'''


# Method 1
'''
num = int(input("Enter any number: "))
org = num
total = 0

while num > 0:
    digit = num % 10

    fact = 1
    for i in range(1, digit + 1):
        fact = fact * i

    total = total + fact
    num = num // 10

if total == org:
    print(f"{org} is a Strong Number.")
else:
    print(f"{org} is not a Strong Number.")
'''

# Method 2 

import math
num = int(input("Enter any number: "))
org = num
total = 0

while num > 0:
    digit = num % 10

    fact = math.factorial(digit)

    total = total + fact
    num = num // 10

if total == org:
    print(f"{org} is a Strong Number.")
else:
    print(f"{org} is not a Strong Number.")