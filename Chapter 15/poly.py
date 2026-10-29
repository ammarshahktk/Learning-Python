# special magic methods / dunder methods
# operatoroverloading
# polymorphism

class Phone: # base class / parent class
    def __init__(self, brand,model_name,price):
        self.brand = brand
        self.model_name = model_name
        self.price = price

    def full_name(self):
            return f"{self.brand} {self.model_name}" 

    #str , repr 

    def __str__(self):
         return f'{self.brand} {self.model_name}'

    def __repr__(self):
         return f'{self.brand} {self.model_name} and price is : {self.price}'

    def __len__(self):
        return len(self.full_name())

    # def __add__(self, other):
    #      return self.price * other.price



class SmartPhone(Phone):
     def __init__(self, brand, model_name, price,camera):
          super().__init__(brand, model_name, price)
          self.camera = camera

     def full_name(self):
          return f"{self.brand} {self.model_name} and price is {self.price} and has a camera of {self.camera}"


my_phone = Phone('Nokia', '1100', 2000)
my_phone2 = Phone('Nokia', '1600', 2200)
my_smartphone = SmartPhone('oneplus', '5t', 33000, '16 MP')
print(my_smartphone.full_name())
print(my_phone.full_name())



# -------------------------------------------------------------
# print(my_phone + my_phone2)
# print(len(my_phone))

# print(repr(my_phone))