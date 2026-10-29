# In this lecture we will leran about how to raise errors

def add(a,b):
    if (type(a) is int ) and (type(b) is int):
       return a + b
    raise TypeError( "OOP's! you are passing wrong data types to function")

print(add( '2' , '3' ))