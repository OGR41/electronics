from main import Products
import pytest


@pytest.fixture()
def product():
    return Products("Чехол", 1500, 15)


# @pytest.fixture()
# def get_discount():
#     product1 = Products("Смартфон", 10000, 20)
#     return product1
