# Ex 30, Take a numebr as input and print the square of that number

def sqr (num):
    return num ** 2 

number = int(input("Enter any number : "))
square = sqr(number)
print(f"the square of {number} is {square}")