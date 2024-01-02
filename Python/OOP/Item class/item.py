import csv
class Item:
    pay_rate=0.8 # The pay rate after 20% discount
    all=[]
    def __init__(self,name:str,price:float ,quantity=0):
    # we dont have to specify the type of quantity cause its by default int
    # Run validation to the received arguments
        assert price>=0,f"Price {price} is not greater or equal than Zero!"   
        # Its a condition to check before completing and we can add our own error message!
        assert quantity>=0,f"Price {quantity} is not greater or equal than Zero!" 
        # Whenever the condtion not valid an error happens
        # Assign to self object
        self.name=name
        self.price=price
        self.quantity=quantity
        # Action to excute
        Item.all.append(self) # We pack all my instances inside my all
    def calculate_total_price(self):
        return  self.price* self.quantity 
    def apply_discount(self):
        self.price = self.price * self.pay_rate #(Best Practice to put here self NOT Item)
    def __repr__(self): # Its a way to represents out objects
        return f"{self.__class__.__name__}('{self.name}',{self.price},{self.quantity})"
    @classmethod# we make the next method as class method,I dont have object to instantiate
    def instantiate_from_csv(cls):
        with open (r"C:\pf\pythonCourse\Python\OOP\Item class\item.csv","r") as file:
            reader=csv.DictReader(file)# it returns an object that maps every line to dict
            items=list(reader)# to list every dict in that object (List of Dictionaries)
            # items=tuple(reader)# we could do that as well.
        for item in items:
            Item(
                # The get() method returns the value of the item with the specified key.
                    name=item.get("name"),
                    price=float(item.get("price")),
                    quantity=int(item.get("quantity"))
                )
    #  lets create our first static method
    # static method never sends the instance as the first argument 
    # unlike the class method that sends the class as first parameter !
    @staticmethod
    def is_integer(num):
        # We will count out the floats that are point zero
        # For i.e 5.0, 10.0
        if isinstance(num, float):
            return num.is_integer()
        # if a float is integer num.0 return True otherwise False
        elif isinstance(num,int):
            return True
        else:
            return False
        

