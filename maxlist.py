ls = []
size = int(input("enter the size of the list"))
print("enter the numbers")
for i in range(size):
    num = int(input())
    ls.append(num)
maxelement= ls[0]
for i in range(size):
    if(ls[i]>maxelement):
        maxelement=ls[i]
print("the max number is "+str(maxelement))

