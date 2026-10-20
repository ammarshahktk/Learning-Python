# in keyword and iteration in dictionary

user_info = {
    'name' :'Ammar',
    'age'  : 20,
    'fav_movies' : ['coco', 'kimi no na wa'],
    'fav_tunes' : ['awakening', 'fairy tale']
} 

# check if key exist in dictionary
# if 'surname' in user_info:
#     print('present')
# else:
#     print('Absent') 


# Check if value exist in dictionary  ------> Vlaue's Method
# if 'Ammar' in user_info.values():
#     print('present')
# else:
#     print('Absent') 


# loops in dictionaries
# for i in user_info.values():
#     print(i)

# values method
# user_info_values = user_info.values()
# print(user_info_values)
# print(type(user_info_values))


#keys method
# user_info_keys = user_info.keys()
# print(user_info_keys)
# print(type(user_info_keys))

# Items Method
# user_items = user_info.items()
# print(user_items)
# print(type(user_items))

for key, value in user_info.items():
    print(f"key is {key} and value is {value}")