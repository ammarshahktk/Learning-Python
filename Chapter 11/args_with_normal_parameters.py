# *args with normal parameters
def multiply_nums ( *args):
    multiply = 1
    # print(num)
    # print(type(num))
    print(args)
    print(type(args))
    for i in args:
        multiply *= i
    return multiply

print(multiply_nums())