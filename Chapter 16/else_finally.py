# else and finally clause in Exception Handling

while True:
    try:
        age = int(input("Enter Your Age : "))#seven
    except ValueError:
        print("Enter your age in numbers")
    except:
        print("Unexpected Error !!! ")
    else:
        print(f"user input = {age}")
        break
    finally:
        print("finally blocks .......")