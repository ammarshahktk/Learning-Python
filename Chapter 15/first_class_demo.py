# OBJECTIVES
# WHAT IS CLASS
# HOW TO CREATE A CLASS
# WHAT IS INIT METHOD, also known as 'constructor'
# WHAT ARE ATTRIBUTES, INSTACE VARIABLES 
# HOW TO CREATE OUR OBJECT

class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age



p1 = Person('Ammar', 'Shah', 19)
p2 = Person('Waris', 'Turk', 23)

print(p1.first_name)
print(p2.first_name)