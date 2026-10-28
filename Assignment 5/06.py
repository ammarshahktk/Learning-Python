# Ex 49, Create a list of numbers from 1 to 20.
    #    Using a loop, separate them into two new lists :One for even numbers, One for odd numbers, Print both lists.

numbers = list(range(1,21))
even_numbers = []
odd_numbers = []        

for nums in numbers:
    if nums % 2 == 0:
        even_numbers.append(nums)
    else:
        odd_numbers.append(nums)

print("Even Numbers : ", even_numbers)
print("Odd Number : ", odd_numbers)