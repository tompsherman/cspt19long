from product import Product
# allows inheritance

#syntax for inheritance class:
class Weapon(Product):
    def __init__(self, name, price, category):
        #reference the init from product using the super() keyword
        super().__init__(name, price)
        self.category = category

    def __str__(self):
            return f"{super().__str__()} is a {self.category} weapon"