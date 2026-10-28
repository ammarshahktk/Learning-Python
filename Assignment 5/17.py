# Ex 60, Create a list of numbers from 1 to 30. Use a loop to:
    #    Add all numbers divisible by 3 to one list , Add all numbers divisible by 5 to another list
    #    Add numbers divisible by both 3 and 5 to a third list.

numbers = list(range(1,31))
divisble_by_three = []
divisble_by_five = []
divisble_by_both = []

for i in numbers:
    if i % 3 == 0:
        divisble_by_three.append(i)
    if i % 5 == 0:
        divisble_by_five.append(i)
    if i % 3 == 0 and i % 5 == 0:
        divisble_by_both.append(i)

print("Numbers divisble by 3 : ", divisble_by_three)
print("Numbers divisble by 5 : ", divisble_by_five)
print("Numbers divisble by both : ", divisble_by_both)