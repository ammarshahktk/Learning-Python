# Decorators - enhance the functionality of other functions

def decorator_function(any_function):
    def wrapper_function(): 
        print("This is awesome function")
        any_function()
    return wrapper_function

# This is awesome function 
@ decorator_function
def func1 ():
    print ("This is function 1 ")
func1()

@ decorator_function
# This is awesome function 
def func2 ():
    print ("This is function 2 ")
func2()