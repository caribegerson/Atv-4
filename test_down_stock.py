from Entities.Product import Product


def test_down_stock():
    # Arrange
    product1 = Product(1, "Product 1", 5.00, 10)

    # Act
    product1.down_stock(5)

    # Assert
    assert product1.stock == 5
