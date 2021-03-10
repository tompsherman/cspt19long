class department:
    def __init__(self, name): #, products):
        self.name = name

    def __str__(self):
        return f"no products in {self.name}"