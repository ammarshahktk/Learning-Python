# Ex 31, Keep asking the user to enter a number and print it. Stop the loop when the user enters 0.(using while True)

while True:
    number = int(input("Enter a number : "))
    if number == 0:
        print("You have entered zero loop has been stopped")
        break

    print(f"You have entered {number}")