# Ex 26, take two numbers as input and return which number is greater 

def greater(num1,num2):
    if num1 > num2:
        return num1
    else:
        return num2

first = int(input("Enter First Number : "))
second = int(input("Enter Second Number : "))

greater_num = greater(first,second)
print(f"The greater number is : {greater_num}")

