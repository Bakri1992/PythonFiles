from item import Item
# If I need methods that are related to phone item so its the best 
# practise to do create a new class that inherits the Item class
class Phone(Item):
    def __init__(self, name: str, price: float, quantity=0,broken_phones=0):
        super().__init__(name, price, quantity)
        assert broken_phones >=0,f"Broken Phones number: {broken_phones} is not valid"
        self.broken_phones=broken_phones