limit = int(input("enter the limit"))
flag=1
for i in range(1,limit):
    for j in range(2,i):
        print("i=",i)
        if(j % i == 0):
            flag=0
    if(flag==1):
        print(i)