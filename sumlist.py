size = int(input("enter the size of the list"))
print("enter the numbers")
ls = [int(input()) for i in range(size)]
print("sum="+str(sum(ls)))