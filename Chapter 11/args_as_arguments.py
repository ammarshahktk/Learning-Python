# when we define a function that is parameter and when we call a function that is called argument 

def multiply_nums (*args):
    multiply = 1
    print(args)
    print(type(args))
    for i in args:
        multiply *= i
    return multiply

nums = (2,3,4)
print(multiply_nums(*nums)) # by writting * items will be upack
