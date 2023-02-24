class Products:
    pay_rate = 1
    all = []

    def __init__(self, title, price, quantity):
        self.title = title
        self.price = int(price)
        self.quantity = int(quantity)
        self.all.append(self)

    def total_price(self):
        return self.price * self.quantity * self.pay_rate

    def discount(self):
        self.price = self.price * self.pay_rate
        return Products(self.title, self.price, self.quantity)


# def main():
#     product1 = Products("Смартфон", 10000, 20)
#     product2 = Products("Ноутбук", 20000, 5)
#
#     print(product1.total_price())
#     print(product2.total_price())
#
#     Products.pay_rate = 0.8
#     product1.discount()
#     print(product1.price)
#     print(product2.price)
#
#     print(Products.all)
#
#
# if __name__ == '__main__':
#     main()