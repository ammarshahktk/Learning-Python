# Ex 22, Password Checker (3 attempts max). Set a fixed password (e.g., "python123")
    #    Allow the user 3 attempts to guess it using while True. If correct, print “Access granted”
    #    If all 3 wrong, print “Account locked”

password = "python123"
attempts = 0
while True:
    user_input = input("Enter Password : ")
    attempts += 1

    if user_input == password:
        print("Access Granted")
        break
    else:
        if attempts == 3:
            print("Account Locked")
            break
        else:
            print(f"Incorrect Password. Remaing Attempts: {3 - attempts} \n ")


