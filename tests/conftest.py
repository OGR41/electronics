from main import Products
import pytest


@pytest.fixture()
def product():
    return Products("Чехол", 1500, 15)
