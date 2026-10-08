number = input("enter a number : ")
#1256
total = 0
i = 0
while i < len(number):
    total += int(number[i])
    i += 1
print(total)