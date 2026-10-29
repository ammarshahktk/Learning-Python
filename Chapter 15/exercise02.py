class Laptop:
    def __init__(self, brand_name, model_name, price):
        self.brand_name = brand_name
        self.model_name = model_name
        self.price = price

    def apply_discount(self,num):
        # self.price
        off_price = (num/100)*self.price
        return self.price - off_price
    


l1 = Laptop('HP', 'au114tx', 40000)
print(l1.apply_discount(40))