from item import Item
class Keyboard(Item):
    payRate = 0.7
    # all = [] - No need it is already define in parent class
    def __init__(self, name: str, price: float, quantity=0, brokenKeyboard = 0):
        
        # call Super class to access all attributes/methods from parent class
        super().__init__(name, price, quantity)
        assert brokenKeyboard >= 0, f"Broken Keyboard {brokenKeyboard} should be greater than or equal to 0"

        self.brokenKeyboard = brokenKeyboard

        