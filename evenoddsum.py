limit = int(input("enter the limit"))
num=input("do you want sum of odd or even numbers\n")
start=0
sumnum=0
if  num=="odd":
    start=1
elif num=="even":
    start=2
else:
    print("invalid number")
    exit
for i in range(start,limit+1,2):
    sumnum+=i
print("sum of"+num+"numbers is",sumnum)
    
