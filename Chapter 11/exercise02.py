# def a function 
# names = ['ammar', 'waris']

# print(func(names))
# print(func(names, reverse_str = True

# function
# list, reverse_str = true
# list

def func(l,**kwargs):
    if kwargs.get('reverse_str') == True:
        return [name[::-1].title() for name in l]
    else:
        return[name.title() for name in l]

names = ['ammar', 'waris']
print(func(names))
print(func(names, reverse_str = True ))