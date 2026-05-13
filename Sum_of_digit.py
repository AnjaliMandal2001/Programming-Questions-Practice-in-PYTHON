# sum of digit


num=1531891
answer=0

while num>0:
    rem=num%10
    answer=answer+rem
    num=num//10
print(answer)