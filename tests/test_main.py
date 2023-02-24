

def test_get_attributes(product):
    assert product.title == 'Чехол'
    assert product.price == 1500
    assert product.quantity == 15
    product.pay_rate = 0.8
    product.discount()
    assert product.price == 1200


def test_get_total_price(product):
    assert product.total_price() == 22500
    product.pay_rate = 0.8
    assert product.total_price() == 18000




