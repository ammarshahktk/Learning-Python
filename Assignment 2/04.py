# Ex 15, Write a program that checks if a person is eligible to vote.A person can vote if they are 18 years or 
    #    older    and a pakistani. Input: age, country . Output: "Eligible to vote" or "Not eligible"

age = int(input("Enter your age : "))
country = input("Enter your country : ")

if age >= 18 and country == 'pakistan':
    print("Eligible to vote.")
else:
    print("Not Eligible.")