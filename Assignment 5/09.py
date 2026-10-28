# Ex 52, Create a list of 6 random numbers.
    #    Find and print the maximum and minimum number using max() and min() functions.

import random
numbers = []
for i in range(6):
    numbers.append(random.randint(1,100))

print("Generated List : ", numbers)
print("Maximum Number : ", max(numbers))
print("Minimum Number : ", min(numbers))
