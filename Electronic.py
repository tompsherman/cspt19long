from product import Product

class Electronic(Product):
    def __init__(self, name, price, voltage):
        super().__init__(name, price)
        self.voltage = voltage

    def __str__(self):
        return f"{super().__str__()} has a voltage of {self.voltage} volts"