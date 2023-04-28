limit = int(input("enter the limit"))
sum=0
for i in range(limit):
    if i==0:
        first=i
        print(i)
    elif i==1:
        second=i
        print(i)
    else:
        sum=first+second
        print(sum)
        first=second
        second=sum
        
