print("hello")
print("Hello world")

## prime or not
num = int(input("Enter a number: "))

if num > 1:
    for i in range(2, num):
        if num % i == 0:
            print("Not a prime number")
            break
    else:
        print("Prime number")
else:
    print("Not a prime number")



## factorial
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

- using math.factorial()
import math

num = int(input("Enter a number: "))
print("Factorial =", math.factorial(num))

## reverse a number
- normal
num = int(input("Enter a number: "))
rev = 0

while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num = num // 10

print("Reversed number =", rev)


-using string slicing
num = input("Enter a number: ")

rev = num[::-1]

print("Reversed number =", rev)



