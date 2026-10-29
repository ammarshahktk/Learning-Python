# class method as a constructor

class Person:
    count_instance = 0  # This is a Class Variable/ Class Attributes

    def __init__(self, first_name, last_name, age):
        Person.count_instance += 1
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    @classmethod
    def from_string(cls, string):
        first,last,age = string.split(',')
        return cls(first,last,age)

    @classmethod
    def count_instances(cls):
        return f"You have created {cls.count_instance} instances of Person Class "


    def full_name(self):
        return f"{self.first_name} {self.last_name}" 

    def is_above_18(self):
        return self.age>18


p1 = Person('Ammar', 'Shah', 19)
p2 = Person('Waris', 'Turk', 22)
p3 = Person.from_string('Ammar,Shah,19')
print(p3.full_name())
# print (Person.count_instances())