# Ex 53, Create a list of country names. Ask the user to input a country name.
    #    Check if the country is in the list and print a message accordingly.

country = ['Pakistan', 'India', 'Bangladesh']
user_input = input("Enter your country : ")

if user_input in country:
    print(f"You are from {user_input} you can proceed forward.")
else:
    print(f"Our networks not work in {user_input}.")