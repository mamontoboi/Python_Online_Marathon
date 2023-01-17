# Create a Pizza class with the attributes order_number and ingredients (which is given as a list).
# Only the ingredients will be given as input.
#
# You should also make it so that its possible to choose a ready made pizza flavour
# rather than typing out the ingredients manually! As well as creating this Pizza class,
# hard-code the following pizza flavours.

class Pizza:
    order = 0

    def __init__(self, ingredients: list):
        self.ingredients = ingredients
        self.order_number = self.order_number_incr()

    @classmethod
    def order_number_incr(cls):
        cls.order += 1
        return cls.order

    @classmethod
    def garden_feast(cls):
        return Pizza(["spinach", "olives", "mushroom"])

    @classmethod
    def hawaiian(cls):
        return Pizza(["ham", "pineapple"])

    @classmethod
    def meat_festival(cls):
        return Pizza(["beef", "meatball", "bacon"])


p1 = Pizza(["bacon", "parmesan", "ham"])

p2 = Pizza.garden_feast()
print(p2.ingredients)

print(p2.order_number)