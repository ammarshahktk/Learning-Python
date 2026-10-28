# Ex 54, Create a list of numbers from 1 to 10.
    #    Use a loop to create a new list containing the squares of each number

numbers = list(range(1,11))
sqr_num = []
for num in numbers:
    sqr_num.append(num**2)

print("Original List : ", numbers)
print("Squared Numbers : ", sqr_num)