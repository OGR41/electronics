import csv
import main
from main import Products
import pytest


@pytest.mark.parametrize('product1', [(Products("Чехол", 1500, 15))])
class TestProducts:

    def test_title(self, product1):
        assert product1.title == 'Чехол'
        assert product1.price == 1500
        assert product1.quantity == 15

    def test_repr(self, product1):
        assert product1.__repr__() == 'Products("Чехол", 1500, 15)'

    def test_str(self, product1):
        assert product1.__str__() == 'Чехол'

    def test_price(self, product1):
        assert product1.price == 1500
        assert product1.total_price() == 22500
        product1.pay_rate = 0.8
        product1.discount()
        assert product1.price == 1200
        assert product1.total_price() == 18000

    def test_len_title(self, product1):
        try:
            product1.title = 'СуперСмартфон'
        except Exception:
            assert "Название не может быть длиннее 10 символов."

    def test_int(self, product1):
        assert float(main.Products.is_integer(product1.price)) == int(main.Products.is_integer(product1.price))

    def test_instantiate_from_csv(self, product1):
        product1.instantiate_from_csv()
        with open(Products.file_name, 'r', encoding='windows-1251') as file:
            reader = csv.reader(file, delimiter=',')
            count = 0
            for i in reader:
                if count == 0:
                    count += 1
                else:
                    Products.all.append(Products(i[0], int(i[1]), int(i[2])))
                    count += 1
        assert len(Products.all) > 0
