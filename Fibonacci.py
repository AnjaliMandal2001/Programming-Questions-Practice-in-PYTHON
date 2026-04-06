num = int(input("Enter the terms: "))

x, y = 0, 1
fibo = 0

while fibo <= num:
    print(fibo)
    x = y
    y = fibo
    fibo = x + y