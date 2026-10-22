# lambdas function (anonymous function)

def add(a,b):
    return a+b

add2 = lambda a,b : a + b
print(add2(2,3))

# We use lamba with our built in functions : map, reduce, filter

multiply = lambda a,b : a * b
print(multiply(2,3))