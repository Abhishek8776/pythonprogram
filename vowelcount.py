st = input("enter the string\n")
vowel="aeiouAEIOU"
count=0
for char in st:
    if char in vowel:
        count += 1
print("Number of vowels:", count)
