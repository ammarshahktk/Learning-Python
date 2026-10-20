# add and delete data 

user_info = {
    'name' :'Ammar',
    'age'  : 20,
    'fav_movies' : ['coco', 'kimi no na wa'],
    'fav_tunes' : ['awakening', 'fairy tale']
} 

# how to add data
# user_info['fav_songs'] = ['song1', 'song2']
# print(user_info)


# POP METHOD
# popped_item = user_info.pop('fav_tunes')
# print(f"popped item is {popped_item}")
# print(user_info)


# POP ITEM METHOD
popped_item = user_info.popitem()
print(user_info)
print(popped_item)