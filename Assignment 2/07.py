# Ex 18, Person must have a job and credit score above 700, and no existing loan.
    #    Input: has_job, credit_score, has_loan. Output: "Eligible for loan" or "Not eligible"

has_job = input("Do you have Job Answer only 'YES' or 'NO' : ")
credit_score = int(input("Enter your credit score : "))
has_loan = input("Do you have any pending loan Answer only 'YES' or 'NO' : ")

if has_job == 'yes' and credit_score>700 and has_loan == 'no':
    print("Eligible for loan")
else:
    print("Not eligible")