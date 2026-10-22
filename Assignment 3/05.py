# Ex 28, Write a function grade_student(marks) that takes marks as input and returns:
    #    “Pass” if marks ≥ 50. “Fail” if marks < 50

def grade_student(marks):
    return "Pass" if marks >= 50 else "Fail"

score = int(input("Enter Your marks : "))
print(grade_student(score))
