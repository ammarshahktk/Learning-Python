# we can drive more than one class from base class ?
# multilevel inheritance
# method resolution order
# method overriding 
# isinstance(), issubclass()


class Phone: # base class / parent class
    def __init__(self, brand,model_name,price):
        self.brand = brand
        self.model_name = model_name
        self.price = price
        self._price = max(price,0)


    def full_name(self):
        return f"{self.brand} {self.model_name}"

    def make_a_call(self,number):
        return f"Calling {number}. .  .   .    ."


class Smartphone(Phone): # derived / Child class
    def __init__(self, brand,model_name,price, ram, internal_memory, rear_camera ):
            # Phone.__init__(self,brand,model_name,price ) # <----uncommon way
            super().__init__(brand,model_name,price) # <----- most used way
            self.ram = ram
            self.internal_memory = internal_memory
            self.rear_camera = rear_camera
    
    
    def full_name(self):
            return f"{self.brand} {self.model_name} and price is {self._price}"
    
    def make_a_call(self,number):
            return f"Calling {number}. .  .   .    ."


class FlagshipPhone(Smartphone):
      def __init__(self, brand,model_name,price, ram, internal_memory, rear_camera, front_camera ):
            super().__init__(brand,model_name,price, ram, internal_memory, rear_camera)
            self.front_camera = front_camera

      def full_name(self):
            
            return f"{self.brand} {self.model_name} and price is {self._price} and front camera = {self.front_camera}"
            
      

# phone = Phone('nokia', '1100', 1000)
smartphone = Smartphone('oneplus', '5', 30000, '6 GB','128GB', '20 MP')
oneplus = FlagshipPhone('iphone', 'x', 40000, '6 GB','128GB', '20 MP', '8 MP')
# print(oneplus.full_name())
# print(help(FlagshipPhone))
# print(smartphone.full_name())

# isinstance:
# print(isinstance(smartphone, Smartphone))
# print(isinstance(oneplus, Phone))
print(issubclass(FlagshipPhone, Smartphone))