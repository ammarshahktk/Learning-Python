# filter function 
def is_even(a):
    return a % 2 == 0

numbers = [3,4,5,2,1,5,6,9,8,10]
# evens = tuple(filter(is_even, numbers))
# evens = tuple(filter(lambda a : a % 2 == 0 , numbers))
# evens = filter(lambda a : a % 2 == 0 , numbers)
# print(evens)

# for i in evens:
#     print(i)

# for i in evens:
#     print(i)

new_evens = [i for i in numbers if i % 2 == 0]
print(new_evens)