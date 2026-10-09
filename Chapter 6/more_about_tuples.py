# looping in tuples
# tuples with one elements
# tuples without paranthesis
# tuple unpacking
# list inside tuple
# some functions that you can use with tuples

mixed = (1,2,3,4.0)

#for loop and tuple:
# for i in mixed:
#     print(i)
# NOTE - you can use while loop too 

# tuple with one element 
nums = (1,)
words = ('word1', )
# print(type(nums))
# print(type(words))

# tuples without paranthesis
# guitars = 'yamaha', 'baton rouge', 'taylor'
# print(type(guitars))

# tuple unpacking

guitarists = ('Maneli Jamal', 'Eddie Ven de Meer', 'Andrew Foy')
guitarists1, guitarists2, guitarists3 = (guitarists)
# print(guitarists2)

# list inside tuples
favorites = ('southern mongolia', ['Tokyo Ghoul Theme', 'landscape'])
favorites[1].pop()
print(favorites)