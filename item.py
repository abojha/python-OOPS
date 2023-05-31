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
        # This double underscore is used to prevent the attribute access from outside
        self.__name = name
        self.__price = price
        self.quantity = quantity

        # Actions to execute
        Item.all.append(self)
    
    @property
    def price(self):
        return self.__price

    def applyDiscount(self):
        self.__price = self.__price * self.payRate

    def applyIncrement(self, incrementValue):
        self.__price = self.__price + self.__price * incrementValue

    # Property Decorator - Read  Only Attributes
    @property
    def name(self):
        return self.__name
    
    # setter can change the value of read only attributes
    @name.setter
    def name(self, value):
        self.__name = value

    def totalPrice(self):
        return self.__price * self.quantity
    
    

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
        return f"{self.__class__.__name__}('{self.name}', {self.__price}, {self.quantity})"