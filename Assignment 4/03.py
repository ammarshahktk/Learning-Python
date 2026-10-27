# Ex 33, (Calculator Menu)        Task:  Create a menu-driven calculator with options:
#        Add, Subtract, Multiply, Divide, Exit     Use while True to keep showing the menu until the user selects 5
#         Sample Menu:    Enter your choice:
#         1. Add
#         2. Subtract
#         3. Multiply
#         4. Divide
#         5. Exit



while True:
    print("---Calculator Menu--- ")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    choice = input("Enter your choice between (1-5):")

    if choice == '5':
        print("Exiting Calculator. Goodbye!")
        break

    if choice in ('1','2','3','4'):
        num1 = int(input("Enter first number : "))
        num2 = int(input("Enter second number : "))

        if choice == '1':
            print(f"{num1} + {num2} = {num1 + num2} ")
        elif choice == '2':
            print(f"{num1} - {num2} = {num1 - num2 } ")
        elif choice == '3':
            print(f"{num1} x {num2} = {num1 * num2}")
        elif choice == '4':
            print(f"{num1} / {num2} = {num1 / num2 }")
    else:
        print("Invalid choice! please select number between 1 to 5.")

