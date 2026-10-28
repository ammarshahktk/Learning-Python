# Ex 59, Create a list of numbers.
    #    Use a loop to multiply each number by 2 and save the results in a new list. Print both the original and new list.

numbers = [3, 7, 12, 5, 20]

doubled_numbers = []

for num in numbers:
    doubled_numbers.append(num*2)

print("Original List : ", numbers)
print("Doubled Numbers List : ", doubled_numbers)