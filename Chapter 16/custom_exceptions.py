# python custom exceptions
# Q - Why custom exceptions ? 
# A - To increase the readability of code.

# example

class NameTooShortError(ValueError):
    pass

def validate(name):
    if len(name) < 8:
        raise NameTooShortError('name is too short')

username = input("Enter your username : ")
validate(username)
print(f"Hello {username}")