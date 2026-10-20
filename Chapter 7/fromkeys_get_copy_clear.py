# From Keys Method
# d = {'name' : 'unknown', 'age' : 'unknown'}

# d = dict.fromkeys(['name', 'age', 'height'], 'unkown')
# print(d) 


# get method (useful) method
d = {'name' : 'unknown', 'age' : 'unknown'}
# print(d['name'])

# print(d.get('name'))
# print(d.get('names')) better


# if 'name' in d :
#     print('present')
# else:
#     print('absent')

# if d.get('name'):
#     print('present')
# else:
#     print('not present')

# If None ------> False, -------> Else True


# clear method
# d.clear()
# print(d)

# clear method
# d1 = d.copy() thse are different dictionaries
#  d1 = d   this is wrong way this is same dictionary
# print(d1)