

def test_get_attributes(product):
    assert product.title == 'Чехол'
    assert product.price == 1500
    assert product.quantity == 15


def test_discount(product):
    assert product.price == 1500
    product.pay_rate = 0.8
    product.discount()
    assert product.price == 1200


def test_get_total_price(product):
    assert product.total_price() == 22500
    product.pay_rate = 0.8
    assert product.total_price() == 18000


def test_len_title(product):
    assert len(product.title) <= 10


def test_len_all(length_all):
    assert len(length_all) > 0


def test_int(integer):
    assert integer == int(integer)


# def test_instantiate_from_csv(instantiate_from_csv):
#     product1 = instantiate_from_csv
#     assert product1.title == 'хлеб'
#     assert product1.price == 50
#     assert product1.quantity == 10
