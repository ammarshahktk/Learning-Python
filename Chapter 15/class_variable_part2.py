class Laptop:
    discount_percent = 10
    def __init__(self, brand_name, model_name, price):
        self.brand_name = brand_name
        self.model_name = model_name
        self.price = price

    def apply_discount(self):
        # self.price
        off_price = (Laptop.discount_percent/100)*self.price
        return self.price - off_price
     
Laptop.discount_percent = 0
l1 = Laptop('HP', 'au114tx', 40000)
print(l1.apply_discount())

print(l1.__dict__)