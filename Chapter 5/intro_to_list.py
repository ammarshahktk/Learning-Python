#data structure
# list ----> this chapter
# ordered collection of items

# you can store anything in lists int, float, string
#we create our list using [square brackets]!!!

number = [1, 2, 3, 4]
print(number[1])

words = ["word1", "word2", 'word3']
print(words[:2])

mixed = [1, 2, 3, 4, 'five', 'six', 2.3, None ]
print(mixed[-1])

mixed[1:]=['two', 'three', 'four']
print(mixed)