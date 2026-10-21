# Ex 16, Write a Python program to decide if a student gets a scholarship:
    #    Scholarship is given if the student has grades above 80 or is from a low-income family.
    #    Input: grade, low_income (True/False). Output: "Scholarship awarded" or "Scholarship denied"

grade = int(input("Enter your grade in marks : "))
income = int(input("Enter your Income : "))

if grade>80 and income <= 40000:
    print("Scholarship Awarded.")
else:
    print("Scholarship denied")