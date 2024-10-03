from src.order import Order


def test_order_object(product_1):
	order = Order(product_1, 8)
	assert order.products == 'Cars, BMW'
	assert order.quantity == 8
	assert order.total_price == 800000


def test_order_quantity(product_1):
	order = Order(product_1, 8)
	order.quantity = 8
	assert order.quantity == 16
