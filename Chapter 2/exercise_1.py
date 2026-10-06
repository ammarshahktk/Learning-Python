# a = input("Enter first number: ")
# b = input("Enter second number: ")
# c = input("Enter third number: ")
# (int(a) + int(b) + int(c)) /3
a, b, c = input("Enter three Numbers comma seperated : ").split(",")
print(f"average of 3 numbers : {(int(a) + int(b) + int(c)) /3}")