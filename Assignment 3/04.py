# Ex 27, palindrom function

def is_palindrom(text):
    return text == text[::-1]

word = input("Enter some words or numbers: ")

if is_palindrom(word):
    print("It is a palindrom")
else:
    print("Is's not a palindrom")