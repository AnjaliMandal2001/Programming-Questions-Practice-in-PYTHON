'''
An Armstrong number is a number equal to the sum of its digits raised to the power of the number of digits.
🔍 Example: 153

Number of digits = 3

Calculation:

(1)3=1
(5)3=125
(3)3=27

Sum = 1 + 125 + 27 = 153 ✅

So, 153 is an Armstrong number

🔍 Another Example: 9474

Digits = 4

(9)4=6561
(4)4=256
(7)4=2401
(4)4=256

Sum = 6561 + 256 + 2401 + 256 = 9474 ✅

So, 9474 is also an Armstrong number
'''



num=int(input("Enter any number:"))
org=num
sum=0

while num>0:
    sum=sum+ (num%10)*(num%10)*(num%10)
    num=num//10

if sum==org:
    print(f"{org} is a Armstrong number.")

else:
    print("It's not a Armstrong number.")