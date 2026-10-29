# Raise Error ex 02:

class Mobile:
    def __init__(self,name):
        self.name = name 


class MobileStore:
    def __init__(self):
        self.mobiles = []

    def add_mobiles(self,new_mobile):
        if isinstance(new_mobile, Mobile):
            self.mobiles.append(new_mobile)
        else:
            raise TypeError('new Mobile should be object of Mobile class')

oneplus = Mobile('one plus 6')
samsung = 'samsung galaxy s25'
mobostore = MobileStore()
# print(mobostore.mobiles)
mobostore.add_mobiles(oneplus)
mobo_phones = mobostore.mobiles
print(mobo_phones[0].name)