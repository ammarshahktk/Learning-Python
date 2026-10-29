# Raise Errors ex 01:
# Not Implemented Errors
# Abstract method


class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self): #<------- this is also called abstract method which body is not defined
        raise NotImplementedError("you have to define this method in sub classes")


class Dog(Animal):
    def __init__(self, name,breed):
        super().__init__(name)
        self.breed = breed

    def sound(self):
        return "Woooh wooh"


class Cat(Animal):
    def __init__(self, name,breed):
        super().__init__(name)
        self.breed = breed

    def sound(self):
            return "meao meao"


doggy = Dog('boony', 'pug')
cato = Cat('shore', 'persian')
print(doggy.sound())
print(cato.sound())
