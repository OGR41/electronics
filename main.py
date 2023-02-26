import csv


class Products:
    pay_rate = 1
    all = []

    def __init__(self, title: str, price, quantity):
        self.__title = title
        self.price = int(price)
        self.quantity = int(quantity)
        self.all.append(self)

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, value):
        if len(value) > 10:
            raise ValueError("Название не может быть длиннее 10 символов.")
        else:
            self.__title = value

    def total_price(self):
        return self.price * self.quantity * self.pay_rate

    def discount(self):
        self.price = self.price * self.pay_rate
        return Products(self.title, self.price, self.quantity)

    @classmethod
    def instantiate_from_csv(cls):
        with open('items.csv', 'r', encoding='windows-1251') as file:
            reader = csv.reader(file, delimiter=',')
            count = 0
            for i in reader:
                if count == 0:
                    count += 1
                else:
                    Products(i[0], int(i[1]), int(i[2]))
                    count += 1

    @staticmethod
    def is_integer(n):
        return int(n) == float(n)


# def main():
#     # product1 = Products("Смартфон", 10000, 20)
#     # product2 = Products("Ноутбук", 20000, 5)
#     #
#     # print(product1.total_price())
#     # print(product2.total_price())
#     #
#     # Products.pay_rate = 0.8
#     # product1.discount()
#     # print(product1.price)
#     # print(product2.price)
#     #
#     # print(Products.all)
#
    # product = Products('Телефон', 10000, 5)
    # product.title = 'Смартфон'
    # print(product.title)
    # product.title = 'СуперСмартфон'
#
    # Products.instantiate_from_csv()
    # print(len(Products.all))
    # product1 = Products.all[0]
    # print(product1.title)
#
#     print(Products.is_integer(5))
#     print(Products.is_integer(5.0))
#     print(Products.is_integer(5.5))
#
#
# if __name__ == '__main__':
#     main()
