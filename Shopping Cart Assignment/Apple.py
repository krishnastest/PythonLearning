import enum
from ProductsAbs import ProductsAbs


class Apple(ProductsAbs):

    def __init__(self, name, price, quantity, categories):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.category = categories

    class Categories(enum.Enum):
        RedApple = "Red"
        GreenApple = "Green"

    def get_quantity(self):
        return self.quantity

    def get_price(self):
        return self.price

    def get_name(self):
        return self.name
