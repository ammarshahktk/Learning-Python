# kwargs (keywords arguments )
# **kwargs (double star operator)

#kwargs as a parameter 

def func(**kwargs):
   for k,v in kwargs.items():
      print(f"{k} : {v}")
    # print(kwargs)
    # print(type(kwargs))

# dictionary unpacking
d = {'name' : 'Ammar', 'age' : 20}
func(**d )

