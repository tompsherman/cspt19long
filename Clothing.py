from product import Product
# allows inheritance

#syntax for inheritance class:
class Clothing(Product):
    def __init__(self, name, price, color):
        #reference the init from product using the super() keyword
        super().__init__(name, price)
        self.color = color

    def __str__(self):
            return f"{super().__str__()} comes in {self.color}"