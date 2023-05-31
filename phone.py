from item import Item
class Phone(Item):
    payRate = 0.6
    # all = [] - No need it is already define in parent class
    def __init__(self, name: str, price: float, quantity=0, brokenPhones = 0):
        
        # call Super class to access all attributes/methods from parent class
        super().__init__(name, price, quantity)
        assert brokenPhones >= 0, f"Broken Phones {brokenPhones} should be greater than or equal to 0"

        self.brokenPhones = brokenPhones

        # Actions to execute
        # Phone.all.append(self)