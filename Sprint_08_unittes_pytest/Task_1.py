# Write the programm that calculate total price with discount by the products.
#
# Use class Product(name, price, count) and class Cart. In class Cart you can add the products.
#
# Discount depends on count product:
#
#
# count	discount
# at least 5	5%
# at least 7	10%
# at least 10	20%
# at least 20	30%
# more than 20	50%

import unittest


class Product:
    def __init__(self, name, price, count):
        self.name = name
        self.price = price
        self.count = count


class Cart:
    def __init__(self, cart):
        self.cart = list(cart)

    def add_product(self, item):
        self.cart.append(item)

    @staticmethod
    def discount(product):
        quantity = product.count
        if 0 <= quantity < 5:
            return 1
        elif quantity < 7:
            return 0.95
        elif quantity < 10:
            return 0.9
        elif quantity < 20:
            return 0.8
        elif quantity == 20:
            return 0.7
        else:
            return 0.5

    def get_total_price(self):
        return sum(self.discount(product) * product.count * product.price for product in self.cart)


class CartTest(unittest.TestCase):
    def setUp(self):
        self.p1 = Product('p1', 10, 4)
        self.p2 = Product('p2', 100, 13)
        self.p3 = Product('p3', 200, 6)
        self.products = [self.p1]
        self.new_product = self.p3
        self.cart = Cart(self.products)

    def test_add_product(self):
        self.cart.add_product(self.new_product)
        self.assertEqual(self.cart.cart, [self.p1, self.p3])

    def test_get_total_price(self):
        self.assertEqual(self.cart.get_total_price(), 40)
        self.cart.add_product(self.new_product)
        self.assertAlmostEqual(self.cart.get_total_price(), 1180)

    def test_discount(self):
        self.assertEqual(self.cart.discount(self.p1), 1)
        self.assertEqual(self.cart.discount(self.p2), 0.8)



products = (Product('p1', 10, 4), Product('p2', 100, 5), Product('p3', 200, 6), Product('p4', 300, 7),
            Product('p5', 400, 9), Product('p6', 500, 10), Product('p7', 1000, 20))
cart = Cart(products)
print(cart.get_total_price())

if __name__ == '__main__':
    unittest.main()