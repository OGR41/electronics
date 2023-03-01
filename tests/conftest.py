# import csv
# from main import Products
# import pytest
# #
#
#
# @pytest.fixture()
# def product1():
#     product1 = Products("Чехол", 1500, 15)
#     return product1
# #
#
# @pytest.fixture()
# def length():
#     product1 = Products("Чехол", 1500, 15)
#     Products.all.append(product1)
#     return Products.all
#
#
# @pytest.fixture()
# def integer():
#     return 10.0
#
#
# @pytest.fixture()
# def instantiate_from_csv():
#     file_name = 'test_item.csv'
#     with open(file_name, 'r', encoding='utf-8') as file:
#         data = csv.reader(file, delimiter=',')
#         return data
#
#
# @pytest.mark.parametrize(Products("Чехол", 1500, 15))
# class TestTitle:
#     def test_title(self):
#         assert