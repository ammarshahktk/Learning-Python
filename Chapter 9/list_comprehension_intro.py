#list comprehension
# with the help of list comprehension we can create of list in one line

# create a list of squares from 1 to 10

# sqaure = []
# for i in range(1,11):
#     sqaure.append(i**2)
# print(sqaure)

# square2 = [i**2 for i in range(1,11)]
# print(square2)

# negative = []
# for i in range(1,11):
#     negative.append(-i)
# print(negative)

# new_negative = [ -i for i in range(1,11)]
# print(new_negative)

names = ['Ammar', 'Arbab', 'Yousuf']
# new_list = ['H', 'M', 'R']
# new_list = []
# for name in name:
#     new_list.append(name[0])

# print(new_list)

new_list2 = [name[4] for name in names]
print(new_list2)