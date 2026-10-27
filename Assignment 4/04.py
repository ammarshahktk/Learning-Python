# Ex 34, Ask the user to enter a password.
    #    Give 3 chances only. If the correct password isn't entered in 3 tries, show a message and exit the loop.

# ----- Trying with while loop -----

# attempts = 0
# max_attempts = 3
# correct_password = "python123"

# while attempts < max_attempts:
#     password = input("Enter password: ")
#     attempts += 1

#     if password == correct_password:
#         print("Access granted!")
#         break
#     else:
#         remaining = max_attempts - attempts
#         if remaining > 0:
#             print(f"Incorrect password. Attempts left : {remaining}")
#         else:
#             print("Account locked too many attempts.")


# ----- Now trying with for loop ------

# correct_password = "python123"
# for attempts in range(1,4):
#     password = input("Enter Password : ")
#     if password == correct_password:
#         print("Access Granted!")
#         break
#     else:
#         if attempts < 3:
#          print(f"Incorrect password. Attempts left: {3 - attempts}")
# else: 
#    print("Account locked too many failed attempts ")
