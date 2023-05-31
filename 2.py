class Item:
    all = []
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

        # Actions to execute
        Item.all.append(self)


    def totalPrice(self):
        return self.price * self.quantity
    
    def applyDiscount(self):
        self.price = self.price * self.payRate

    # __repr__ representation purpose magic method
    def __repr__(self):
        return f"Item('{self.name}', {self.price}, {self.quantitya})"



item1 = Item("Phone", 100, 1)
item2 = Item("Laptop", 1000, 3)
item3 = Item("Cable", 10, 5)
item4 = Item("Mouse", 50, 6)
item5 = Item("Keyboard", 75, 5)


print(Item.all)
# Traverse each instance of an Class
# for instance in Item.all:
#     print(instance.name)

