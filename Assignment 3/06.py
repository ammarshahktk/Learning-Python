# Ex 29, Write a function print_table(n) that prints the multiplication table of a number n.

def print_table(n):
    table = ""
    for i in range(1,11):
        table += f"{n} x {i} = {n * i} \n"
    return table    

number = int(input("Enter a number to prints its table : "))
print(print_table(number))