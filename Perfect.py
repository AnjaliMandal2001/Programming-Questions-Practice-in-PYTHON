'''
A perfect number is a number that is equal to the sum of its proper divisors (excluding the number itself).

📌 Example: 6

Divisors of 6 → 1, 2, 3, 6
Proper divisors → 1, 2, 3

Sum = 1 + 2 + 3 = 6 ✅
So, 6 is a perfect number

📌 Another Example: 28

Divisors → 1, 2, 4, 7, 14, 28
Proper divisors → 1, 2, 4, 7, 14

Sum = 1 + 2 + 4 + 7 + 14 = 28 ✅
So, 28 is also a perfect number
'''

num=int(input("Enter any number:"))
org=num
start=1
answer=0

while start<num:
    if num%start==0:
        answer=answer+start
    start = start + 1

if org==answer:
    print(f"{org} is a Perfect number.")
else:
    print(f"{org} is not a Perfect number.")