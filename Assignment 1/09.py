# Ex 9, take two inputs from user, his name and a character. check the length of his name and count the character

name = input("Enter your name : ")
char = input("enter any charachter : ")
name_length = len(name)
char_count = name.lower().count(char.lower())
print(f"Length of your name is : ", {name_length})
print(f"the charachter '{char} appear {char_count} time's in your name.")