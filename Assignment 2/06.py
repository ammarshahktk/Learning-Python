# Ex 17, Ask the user to input two numbers and compare them using comparison operators (>, <, ==).
    #    Print which number is greater or if they are equal.also print that which number is grater.

num1 = int(input("Enter Frist Number : "))
num2 = int(input("Enter Second Number : "))

if num1 > num2:
    print(f"{num1} is greater than {num2} ")
elif num1 == num2:
    print(f"{num2} is equal to {num1}")
else:
    print(f"{num2} is greater than {num1}")