# Exception Handling 
# exceptions are the errors which occur during the execution time
# try except else finally
while True:
    try:
        age = int(input("Enter Your Age : "))#seven
        break
    except ValueError:
        print("Enter your age in numbers")

if age < 18:
    print("you can't play this game.")
else:
    print("you can play this game.")