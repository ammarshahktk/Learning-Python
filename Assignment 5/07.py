# Ex 50, Given a list with repeated values:
    #    numbers = [1, 2, 2, 3, 4, 4, 5 ]. Create a new list that contains only the unique values.

numbers = [1, 2, 2, 3, 4, 4, 5 ]

unique_numbers = []

for num in numbers:
    if num not in unique_numbers:
        unique_numbers.append(num)

print("Original List : ",numbers)
print("Unique List : ", unique_numbers)
