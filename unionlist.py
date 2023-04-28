size1 = int(input("enter the size of the list"))
print("enter the numbers")
ls1 = [int(input()) for i in range(size1)]
size2 = int(input("enter the size of the list"))
print("enter the numbers")
ls2 = [int(input()) for i in range(size2)]
ls3 = list(set(ls1).union(set(ls2)))
print("union\n",ls3)