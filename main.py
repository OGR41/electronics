import csv


class Products:
    pay_rate = 1
    all = []
    file_name = 'items.csv'

    def __init__(self, title: str, price, quantity):
        self.__title = title
        self.price = price
        self.quantity = quantity

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
        return self.price * self.quantity

    def discount(self):
        self.price = self.price * self.pay_rate
        return Products(self.title, self.price, self.quantity)

    @classmethod
    def instantiate_from_csv(cls):
        with open(Products.file_name, 'r', encoding='windows-1251') as file:
            reader = csv.reader(file, delimiter=',')
            count = 0
            for i in reader:
                if count == 0:
                    count += 1
                else:
                    Products.all.append(Products(i[0], int(i[1]), int(i[2])))
                    count += 1

    @staticmethod
    def is_integer(n):
        return int(n) == float(n)

    def __repr__(self):
        return f'{self.__class__.__name__}("{self.title}", {self.price}, {self.quantity})'

    def __str__(self):
        return f'{self.title}'


# def main():
#     product1 = Products('Смартфон', 10000, 20)
#     product1
#     print(product1)
#
#
# if __name__ == '__main__':
#     main()
