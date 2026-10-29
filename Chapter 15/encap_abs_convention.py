# In this topic we will talk about
# Encapsulation
# Ecapsulation means to write your data and function at same class/place is called encapsulation
# Abstraction

# Some special naming convention
# Name Mangling


class Phone:
    def __init__(self, brand, model_name, price):
        self.brand = brand
        self.model_name = model_name
        self.__price = price

    def make_a_call(self, phone_number):
        print(f"Calling {phone_number} ...")

    def full_name(self):
        return f"{self.brand} {self.model_name}"

    def send_message(self):
        pass  # twilio


phone1 = Phone('nokia', '1100', 1100)
print(phone1._Phone__price)
print(phone1.__dict__)
# l = [3,4,1,2]
# l.sort() # tim sort
# print(l)