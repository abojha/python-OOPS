class Item:
    # Class Attribute
    payRate = 0.8 # The Pay rate after 20% discount
    # Constructor __init__
    def __init__(self, name: str, price: float, quantity=0):
        # Run Validation to the Recieiver Arguments
        assert price >= 0, f"Price {price} should be greater than or equal to 0"
        assert quantity >= 0, f"Quantity {quantity} should be greater than or equal to 0"
        # Assign to self Object
        # Instance Attributes
        self.name = name
        self.price = price
        self.quantity = quantity


    def totalPrice(self):
        return self.price * self.quantity
    
    def applyDiscount(self):
        self.price = self.price * self.payRate

# Static Assignments
# # Item1
# item1 = Item("Phone", 100)
# item1.price = 
# item1.quantity = 5
# # print(item1.totalPrice(item1.price, item1.quantity))

# # Item2
# item2 = Item("Laptop")
# item2.price = 150
# item2.quantity = 10
# # print(item2.totalPrice(item2.price, item2.quantity))

# Dynamic Assignments
item1 = Item("Phone", 100, 5)
item2 = Item("Laptop", 100, 10)

# We can assign new attributes to an instance individually
item2.hasNumpad = False 

# Access function through instances
# print(item1.totalPrice())
# print(item2.totalPrice())

# Access Class attribute by Class Name
# print(Item.payRate)

# Acess Class Attribute by Instance Name
# it sees the attribute at instance level first and then go to class level
# print(item1.payRate)
# print(item2.payRate)

# print(Item.__dict__) # All the Attributes at the Class Level
# print(item1.__dict__) # All the Attributes at the Instance Level

item1.applyDiscount()
print(item1.price)

item2.payRate = 0.7
item2.applyDiscount()
print(item2.price)