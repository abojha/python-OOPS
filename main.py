from item import Item
from phone import Phone
from keyboard import Keyboard

item1 = Item("MyItem", 1000)
phone1 = Phone("Samsung", 1000)
keyboard1 = Keyboard("HP", 1000)

# Magic of Polymorphism
item1.applyDiscount() # use payRate default from parent class
phone1.applyDiscount() # use payRate from their own class
keyboard1.applyDiscount() # use payRate from their own class
print("Hi how are you")

print(item1.price)
print(phone1.price)
print(keyboard1.price)
