#Find largest among three numbers


num1=int(input("Enter first number:"))
num2=int(input("Enter second number:"))
num3=int(input("Enter third number:"))


 # method1- Using if-else 
if num1>num2 and num1>num3:
    print(num1, "is a greater number.")
elif num2>num1 and num2>num3:
    print(num2,"is a greater number.")
else:
    print(num3,"is a grater number.")

#method2- Using Max() 
ans=max(num1,num2,num3)
print("Greater number among three is :",ans)




