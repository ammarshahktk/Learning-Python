# Ex 48, Ask the user to enter 5 numbers (one by one) and store them in a list using append().
    #    Print the final list.


numbers = []
for i in range(1 , 6):
    num = int(input(f"Enter number {i} of 5: "))
    numbers.append(num)

print("Collected numbers : ", numbers)