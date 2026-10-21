# Ex 19, Simple Grade Evaluator. Input: Marks from 0 to 100
    #    Use conditions: 90+ → A1 , 80–89 → A , 70–79 → B , below 70 → Fail

marks = int(input("Enter yours Marks : "))

if marks>=90:
    print("A1 Grade !")
    print("Congrats")
elif marks>=80:
    print("A Grade !")
    print("Good")
elif marks>=70:
    print("B Grade !")
    print("Try to improve next time")
else:
    print("Fail !")
    print("Try Again ")

    