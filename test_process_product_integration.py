from datetime import datetime

from Entities.Customer import Customer
from Entities.Order import Order
from Entities.OrderProduct import OrderProduct
from Entities.Product import Product


def test_process_product_integration():
    # Arrange
    customer1 = Customer(1, "Customer 1")
    product1 = Product(1, "Product 1", 5.00, 10)
    order1 = Order(1, customer1, datetime.today())
    order_line1 = OrderProduct()

    # Act
    order_line1.add_product(product1, 5)
    
    order1.add_order_product(order_line1)
    order1.update_total_price()

    # Assert
    assert order1.total_price == product1.price * order_line1.quantity
