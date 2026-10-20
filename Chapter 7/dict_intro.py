# dictionaries intro 
# Q - Why we use dictionaries
# A - Because of Limitations od list, lists are not enough to represent real data.
# Example
# user = ['Ammar', 24, ['coco', 'kimi no na wa'],['awakening', 'fairy tale']]
# this list contains username, age, fav movies, fav tunes, 
# you can do this but this is not a good way to do this.

# Q - what are dictionaries?
# A - unordered collection of data in key : value pair.

#  How to create dictionaries
# user = {'name' : 'Ammar', 'age' : 20}
# print(user)
# print(type(user))

# second method to create dictionaries
user_1 = dict(name = 'Ammar', age = 20)

# how to access data from dictionaries
# NOTE - There is no indexing because of unordered collections of data 
# print(user['name'])
# print(user['age'])

# which type of data dictionaries can Store ?
# anything
# numbers, list,  strings, dictionaries

user_info = {
    'name' :'Ammar',
    'age'  : 20,
    'fav_movies' : ['coco', 'kimi no na wa'],
    'fav_tunes' : ['awakening', 'fairy tale']
} 

# print(user_info['fav_movies'])

# how to add data into empty dictionary
user_info2 = {}
user_info2['name'] = 'ammar'
print(user_info2)