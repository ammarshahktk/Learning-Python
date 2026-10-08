#sum from 1 to 10...
#1+2+3+.......10
# total = 0
# for i in range(1,11):
#     total += i
#     print(total)

num = int(input("enter the number : "))
total = 0
for i in range(1,num+1):
    total += i

print(total)
