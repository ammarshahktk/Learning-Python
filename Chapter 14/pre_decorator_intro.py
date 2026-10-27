# You have to complete understanding of functions
# first class function / closures 
# then finally we will learn about decorators 


def square(a):
    return a**2

s = square
print(square(7))
print(s.__name__)