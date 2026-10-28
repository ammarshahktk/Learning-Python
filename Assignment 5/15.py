# Ex 58, Create a list of numbers from 1 to 20.
    #    Use a loop to remove all even numbers. Print the final list of odd numbers.

numbers = list(range(1,21))
odd_num = []

for i in numbers:
    if i % 2 != 0:
        odd_num.append(i)

print("final list of all odd numbers: ", odd_num)