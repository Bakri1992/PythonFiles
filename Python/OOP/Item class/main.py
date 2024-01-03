from item import Item
from phone import Phone
item1=Item("MyItem",750,1)
print(item1.name) # Each private member can I get using getter method
print(item1._Item__name) # We can get the private 
