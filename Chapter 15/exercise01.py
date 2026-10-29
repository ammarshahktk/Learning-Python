class Laptop:
    def __init__(self, brand_name, model_name, price):
        self.brand_name = brand_name
        self.model_name = model_name
        self.price = price

l1 = Laptop('HP', 'au114tx', 40000)
l2 = Laptop('DELL', 'Inspiron 15', 30000)

print(l1.brand_name, l1.model_name, l1.price)
print(l2.brand_name, l2.model_name, l2.price)