import csv
import os.path


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
        try:
            with open(Item.file_name, 'r', encoding='windows-1251') as file:
                reader = csv.DictReader(file, delimiter=',')
                for row in reader:
                    if list(row.keys()) == ['name', 'price', 'quantity']:
                        cls(title=row['name'], price=row['price'], quantity=row['quantity'])
                    else:
                        raise InstantiateCSVError
                count = 0
                for i in reader:
                    if count == 0:
                        count += 1
                    else:
                        Item.all.append(Item(i[0], int(i[1]), int(i[2])))
                        count += 1
        except FileNotFoundError:
            error_info = 'FileNotFoundError: Отсутствует файл item.csv'
            print(error_info)
        except InstantiateCSVError:
            error_info = 'InstantiateCSVError: Файл item.csv поврежден'
            print(error_info)

    @staticmethod
    def is_integer(n):
        return int(n) == float(n)

    def __repr__(self):
        return f'{self.__class__.__name__}("{self.__title}", {self.price}, {self.quantity})'

    def __str__(self):
        return f'{self.__title}'


class InstantiateCSVError(Exception):
    def __init__(self):
        super().__init__()


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


class MixinLog:

    @property
    def language(self):
        return str(kb.__repr__())
        # f:
        #     return str(kb.__repr__())
        # elif kb._Keyboard__lang == 'RU':
        #     return str(kb.__repr__())
        # else:
        #     return "AttributeError: property 'language' of 'KeyBoard' object has no setter"

    def change_lang(self):
        if kb._Keyboard__lang == "EN":
            kb._Keyboard__lang = 'RU'
        elif kb._Keyboard__lang == "RU":
            kb._Keyboard__lang = 'EN'


class Keyboard(Item, MixinLog):
    def __init__(self, *args, lang='EN'):
        super().__init__(*args)
        self.__lang = lang

    def __repr__(self):
        return self.__lang


# Item.instantiate_from_csv()
kb = Keyboard('D_P_KD87A', 9600, 5)
# print(kb)
# print(kb.language)
# kb.change_lang()
# print(kb.language)
# kb.language = 'CH'
