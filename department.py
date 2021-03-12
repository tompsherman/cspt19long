class department:
    def __init__(self, name, products):
        self.name = name
        self.products = products

    def __str__(self):
        output = f"{self.name}\n"
        if len(self.products) > 0:
            for product in self.products:
                output += f"\t{product}\n"
        else:
            output += f"there are no products in here"

        return output

