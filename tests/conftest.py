import pandas as pd
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


# @pytest.fixture()
# def instantiate_from_csv():
#     data = pd.read_csv("test_item.csv", delimiter=',')
#     reader = data.values.tolist()
#     return Products(reader[0][0], reader[0][1], reader[0][2])


