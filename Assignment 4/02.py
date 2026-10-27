# Ex 32, (Simple Login System)  Keep asking for a username and password until the user enters the correct 
    #    combination (e.g., "admin" and "1234").Use break when login is successful.

admin = "admin"
password = "1234"

while True:
    user_admin = input("Enter user name : ")
    user_pass = input("Enter Password : ")
    if user_admin == admin and user_pass == password:
        print("Login Successful")
        break
    print("Incorrect username or password. Try again.\n")