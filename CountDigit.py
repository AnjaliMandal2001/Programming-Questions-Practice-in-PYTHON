#count total digit
num=153189175
count_digit=0

while num>0:
    rem=num%10
    count_digit=count_digit+1
    num=num//10
print(count_digit)
