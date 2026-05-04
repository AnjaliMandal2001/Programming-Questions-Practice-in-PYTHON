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