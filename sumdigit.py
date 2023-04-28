num=int(input("enter a number"))
temp=num
sum=0
while temp>0:
    digit=temp%10
    sum=sum+digit
    temp=temp//10
print("sum of digits is ",sum)