#scope
x = 5 # global variable

def func():
    global x
    x = 7
    return x  #local variable

print(x)
print(func())
print(x)
