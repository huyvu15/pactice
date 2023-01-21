# lập trình hướng đối tượng


# define a class in python

#
class Product:
    default_discount = 0
    def __init__(self, price):
        self.price = price
        self.discount = Product.default_discount

    def set_discount(self, discount):
        self.discount = discount

    def net_price(self):
        return self.price * (1 - self.discount)
    
p1 = Product(100)
print(p1.net_price())
p2 = Product(200)
p2.set_discount(0.05)
print(p2.net_price())

    