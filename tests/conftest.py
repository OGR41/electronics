import csv
from main import Products
import pytest



@pytest.fixture()
def product():
    return Products("Чехол", 1500, 15)


@pytest.fixture()
def length_all():
    product = Products("Чехол", 1500, 15)
    Products.all.append(product)
    return Products.all


@pytest.fixture()
def integer():
    return 10.0


@pytest.fixture()
def instantiate_from_csv():
    with open('items.csv', 'r', encoding='windows-1251') as file:
        reader = csv.reader(file, delimiter=',')
        count = 0
        for i in reader:
            if count == 0:
                count += 1
            else:
                Products(i[0], int(i[1]), int(i[2]))
                count += 1
    return Products.all[0]


