from department import department
from product import Product
from Clothing import Clothing
from Weapon import Weapon

class store:
    def __init__(self, name, departments):
        #attributes -- elements inside class (self.etc)
        self.name = name
        self.departments = departments

    def __str__(self):
        output = f"{self.name}\n"

        for i, dept in enumerate(self.departments):
            output += f"  [{i+1}]  {dept.name}\n"

        output += f"  [{len(self.departments)+1}]  Exit"
        output += "\n"

        return output
        
my_store = store("bobs emporium", [department("clothes", [Clothing("t-shirt", 100, "red")]), department("weapons", [Weapon("firearm", 300, "melee")]), department("electronics", []), department("kitchenware", [])])

choice = 0
while choice != len(my_store.departments)+1:
    print(my_store)
    choice = int(input("Please choose a floor:"))

    if choice == len(my_store.departments)+1:
        print("thanks for shopping!")
    elif choice > 0 and choice <= len(my_store.departments):
        print(f"{my_store.departments[choice-1]}")
    else:
        print("select valid floor")

    print(choice)
