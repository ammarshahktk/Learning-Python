# Ex 35, Ask the user to enter numbers. Print if the number is even or odd. Stop if the number is negative.

while True:
    number = int(input("Enter a Number : "))

    if number < 0 :
        print("You have entered a negative number. Stopping the program.")
        break

    if number % 2 == 0:
        print("entered number is even")
    else:
        print("entered number is odd")