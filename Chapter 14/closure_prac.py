# function returning (closure) practice
# it is also called first class function 
# making a function which return square or cube or power 4 for doing this we have to make multiple function for each part but in funtion returning function we can do all this in one 

def to_power(x):
    def calculate_power(n):
        return n ** x
    return calculate_power

cube = to_power(3)
print(cube(2))