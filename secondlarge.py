ls = []
size = int(input("enter the size of the list"))
print("enter the numbers")
for i in range(size):
    num = int(input())
    ls.append(num)
for i in range(size):
    for j in range(i+1,size):
        if(ls[i]>ls[j]):
            ls[i],ls[j]=ls[j],ls[i]
print("second largest element is")
print(str(ls[-2]))