def decorator_function(any_function):
    def wrapper_function(): 
        print("This is awesome function")
        any_function()
    return wrapper_function

# This is awesome function 
@ decorator_function
def func ():
    print ("This is awesome function")
func() 