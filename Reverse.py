## reverse a number


#method 1- normal
num = int(input("Enter a number: "))
rev = 0

while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num = num // 10

print("Reversed number =", rev)



#method2-using string slicing
num = input("Enter a number: ")

rev = num[::-1]

print("Reversed number =", rev)