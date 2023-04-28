num = int(input("Enter a number: "))
sum = 0
power = len(str(num))
temp = num
while temp > 0:
    digit = temp % 10
    sum += digit ** power
    temp //= 10
print(sum)
if num == sum:
    print(num,"is an Armstrong number")
else:
    print(num,"is not an Armstrong number")
