#syntax for a class:
#class NameOfClass:

#class / blueprint of object we want to make
class Animal:

    def __init__(self, name, colors):
    #build out shape of object
    #self is reference to object instantiates, same as "this" in JS
        self.name = name
        self.age = 1
        self.fav_colors = colors

    def __str__(self):
        output = f"My name is {self.name} and I am {self.age} years old.\n"
        output += "My favorite colors are:"
        for col in self.fav_colors:
            output += f"{col} "
        output += "\n"

        return output

    #representation of object
    #repr is for developers to debug things
    # ideally should return how you made an object
    def __repr__(self):
        return "I am a fish"

my_colors = ["red", "yellow", "cyan"]
dog = Animal("Dave", my_colors)
cat = Animal("Sue", ["orange", "blue"])

print(dog)
print(cat)
"""
holds data and methods to act upon that data
"""