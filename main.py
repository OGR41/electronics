import csv


class Item:
    pay_rate = 1
    all = []
    file_name = 'items.csv'

    def __init__(self, title: str, price, quantity):
        self.__title = title
        self.price = price
        self.quantity = quantity
        self.len_title = title

    @property
    def len_title(self):
        return str(self.__title)

    @len_title.setter
    def len_title(self, value):
        if len(value) > 10:
            raise ValueError("Название не может быть длиннее 10 символов.")
        else:
            self.__title = value

    def total_price(self):
        return self.price * self.quantity

    def discount(self):
        self.price = self.price * self.pay_rate
        return Item(self.__title, self.price, self.quantity)

    @classmethod
    def instantiate_from_csv(cls):
        with open(Item.file_name, 'r', encoding='windows-1251') as file:
            reader = csv.reader(file, delimiter=',')
            count = 0
            for i in reader:
                if count == 0:
                    count += 1
                else:
                    Item.all.append(Item(i[0], int(i[1]), int(i[2])))
                    count += 1

    @staticmethod
    def is_integer(n):
        return int(n) == float(n)

    def __repr__(self):
        return f'{self.__class__.__name__}("{self.__title}", {self.price}, {self.quantity})'

    def __str__(self):
        return f'{self.__title}'


class Phone(Item):
    def __init__(self, title: str, price, quantity, sim_quantity):
        super().__init__(title, price, quantity)
        self.number_of_sim = sim_quantity

    def __add__(self, other):
        if not isinstance(other, Item):
            raise ValueError('Запрещено')
        else:
            return self.quantity + other.quantity

    @property
    def number_of_sim(self):
        return self.sim_quantity

    @number_of_sim.setter
    def number_of_sim(self, value):
        if value < 1:
            raise ValueError('Количество физических SIM-карт должно быть целым числом больше нуля.')
        else:
            self.sim_quantity = value

    def __repr__(self):
        return f'{self.__class__.__name__}("{self.len_title}", {self.price}, {self.quantity}, {self.sim_quantity})'


# item1 = Item('Суперсмартфон', 2000, 20)
# item = Item('Чехол', 2000, 20)
# print(str(item))
# phone = Phone("iPhone 14", 120_000, 5, 2)
# print(phone.__repr__())
# def main():
#     phone = Phone("iPhone 14", 120_000, 5, 2)
#     print(phone)
#     print(repr(phone))
#     phone.number_of_sim = 0
#
#
# if __name__ == '__main__':
#     main()
