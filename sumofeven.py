n=int(input("enter the limit"))
print("sum of even numbers upto "+str(n)+" is")
sum=0
for i in range(1,n):
    if(i%2==0):
        sum=sum+i
print(sum)

