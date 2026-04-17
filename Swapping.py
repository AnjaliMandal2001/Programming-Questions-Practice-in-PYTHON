# Swapping two numbers
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("Using temp variable -------")
print("Before swapping:", num1, "and", num2)

# Method 1- Using temp variable
temp = num1
num1 = num2
num2 = temp

print("After swapping using temp:", num1, num2)


# Method 2 -Using tuple unpacking / multiple assignment
num3 = 89
num4 = 34

print("\nUsing tuple unpacking -------")
print("Before swapping:", num3, "and", num4)

(num3, num4) = (num4, num3)

print("After swapping using tuple unpacking:", num3, num4)