#number Guessing game
# -------------elif statement--------------
winning_number = 12
guess_number = input("Guess your number between 1 - 20 : ")
guess_number = int(guess_number)
if guess_number==winning_number:
    print("You win!!!")

elif guess_number>winning_number:
    print("Your guess is higher than actual number!!")
    print("Try Again")
    

else:
    print("Your guess is lower than actual number!!")
    print("Try Again")