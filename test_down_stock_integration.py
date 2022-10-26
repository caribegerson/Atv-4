from Entities.OrderProduct import OrderProduct
from Entities.Product import Product


def test_down_stock_integration():
    # Arrange
    product1 = Product(1, "Product 1", 5.00, 10)
    order_line1 = OrderProduct()
    order_line2 = OrderProduct()

    # Act
    order_line1.add_product(product1, 5)
    order_line2.add_product(product1, 6)

    # Assert
    assert product1.stock == 5
