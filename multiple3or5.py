limit = int(input("enter the limit"))
num=int(input("enter 3 or 5"))
sum=0
for i in range(1,limit+1):
    if(i%num==0):
        sum=sum+i
print(f"sum of all multiples of {num} is",sum)
