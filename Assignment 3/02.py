# Ex 24, function of odd even checker number

# def odd_even(num):
#     if num % 2 == 0:
#         print("Number is Even")
#     else:
#         print("Number is odd")

# user = int(input("Enter any number to check : "))
# odd_even(user)

# Ex 25, function returning boolean value (True or False)

def is_even(num):
    return num % 2 == 0

number = int(input("Enter a number : "))
print(is_even(number))