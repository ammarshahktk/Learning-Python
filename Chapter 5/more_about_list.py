#generate list with range function
# something more about pop method
# index method 
# pass list to a function

# numbers = list(range(1,11 ))
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1]
# print(numbers)
# popped_items = numbers.pop() # will return only value which is pop like in this case it will retrn 10
# print(numbers) 

# print(numbers.index(1, 3))

def negative_list(l):
    negative = []
    for i in l:
        negative.append(-i)
    return negative

print(negative_list(numbers))