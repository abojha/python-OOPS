import csv
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

    # Write class Method
    @classmethod
    def instantiateFromCSV(cls):
        with open("item.csv", 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)
        
        # Instantiate object from items
        for item in items:
            # print(item)
            Item(
                name=item.get('name'),
                price=float(item.get('price')),
                quantity=int(item.get('quantity'))
            )

    # Static Method - No need to send either self or cls
    @staticmethod
    def isInteger(num):
        # We will count out the floats that are point zero
        if isinstance(num, float):
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False


    # __repr__ representation purpose magic method
    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"



# Inheritence
class Phone(Item):
    # all = [] - No need it is already define in parent class
    def __init__(self, name: str, price: float, quantity=0, brokenPhones = 0):
        
        # call Super class to access all attributes/methods from parent class
        super().__init__(name, price, quantity)
        assert brokenPhones >= 0, f"Broken Phones {brokenPhones} should be greater than or equal to 0"

        self.brokenPhones = brokenPhones

        # Actions to execute
        # Phone.all.append(self)


# Phone1 = Item("SamsungA21s", 20000, 15)
# Phone1.brokerPhone = 5
# Phone2 = Item("Iphone 14", 40000, 15)
# Phone2.brokenPhone = 2

Phone1 = Phone("SamsungA21s", 20000, 15, 1)

# print(Phone1.totalPrice())

print(Item.all)
print(Phone.all)