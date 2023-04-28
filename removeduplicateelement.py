ls = []
size = int(input("enter the size of the list"))
print("enter the numbers")
for i in range(size):
    num = int(input())
    ls.append(num)
newel = []
for i in range(size):
    if ls[i] not in newel:
        newel.append(ls[i])
print(newel)



