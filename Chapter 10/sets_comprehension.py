# sets comprehension ----> only one video 
s = {k**2 for k in range(1,11)}
print(type(s))
print(s)

names = ['ammar', 'barbab', 'yousuf']
first = {name[0] for name in names}
print(first)