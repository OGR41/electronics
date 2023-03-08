import csv
import main
from main import Item, Phone, Keyboard
import pytest


@pytest.mark.parametrize('item1', [(Item("Чехол", 1500, 15))])
class TestItem:

    def test_title(self, item1):
        assert item1.len_title == 'Чехол'
        assert item1.price == 1500
        assert item1.quantity == 15

    def test_repr(self, item1):
        assert item1.__repr__() == 'Item("Чехол", 1500, 15)'

    def test_str(self, item1):
        assert item1.__str__() == 'Чехол'

    def test_price(self, item1):
        assert item1.price == 1500
        assert item1.total_price() == 22500
        item1.pay_rate = 0.8
        item1.discount()
        assert item1.price == 1200
        assert item1.total_price() == 18000

    def test_len_title(self, item1):
        try:
            item1.len_title = 'СуперСмартфон'
        except Exception:
            assert "Название не может быть длиннее 10 символов."

    def test_int(self, item1):
        assert float(main.Item.is_integer(item1.price)) == int(main.Item.is_integer(item1.price))

    def test_instantiate_from_csv(self, item1):
        item1.instantiate_from_csv()
        with open(Item.file_name, 'r', encoding='windows-1251') as file:
            reader = csv.reader(file, delimiter=',')
            count = 0
            for i in reader:
                if count == 0:
                    count += 1
                else:
                    Item.all.append(Item(i[0], int(i[1]), int(i[2])))
                    count += 1
        assert len(Item.all) > 0


@pytest.mark.parametrize('phone1 ', [Phone("iPhone 14", 120000, 5, 2)])
class TestPhone:
    def test_title(self, phone1):
        assert phone1.len_title == 'iPhone 14'
        assert phone1.price == 120_000
        assert phone1.quantity == 5
        assert phone1.number_of_sim == 2

    def test_number_of_sim(self, phone1):
        try:
            phone1.number_of_sim = 0
        except Exception:
            assert "Количество физических SIM-карт должно быть целым числом больше нуля."

    def test_repr_phone(self, phone1):
        assert phone1.__repr__() == 'Phone("iPhone 14", 120000, 5, 2)'


@pytest.mark.parametrize('kb', [Keyboard('D_P_KD87A', 9600, 5)])
class TestKeyboard:
    def test_title(self, kb):
        assert kb.len_title == 'D_P_KD87A'
        assert kb.price == 9600
        assert kb.quantity == 5
        assert kb.language == 'EN'

    def test_change_lang(self, kb):
        kb.language = 'EN'
        kb.change_lang()
        assert kb.language == 'RU'
        kb.change_lang()
        assert kb.language == 'EN'
        with pytest.raises(AttributeError):
            kb.language = 'CH'
