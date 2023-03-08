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


class MixinLog:
    @property
    def language(self):
        return str(self.__lang)

    @language.setter
    def language(self, value):
        if 'RU' != value != 'EN':
            raise AttributeError("property 'language' of 'KeyBoard' object has no setter")
        else:
            self.__lang = value

    def change_lang(self):
        if self.__lang == "EN":
            self.__lang = 'RU'
        elif self.__lang == "RU":
            self.__lang = 'EN'


class Keyboard(Item, MixinLog):
    def __init__(self, *args, lang='EN'):
        super().__init__(*args)
        self.__lang = lang
        self.language = lang


# kb = Keyboard('D_P_KD87A', 9600, 5)
# print(kb)
# print(kb.language)
# kb.change_lang()
# print(kb.language)
# kb.language = 'CH'
