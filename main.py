import json
import logging

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(module)s %(levelname)s: %(message)s',
                    filename=r'logs/main_logs.log',
                    filemode='w')
logger = logging.getLogger(__name__)

logger.info("Using module main")


class Product:
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    def __str__(self):
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        return self.__price * self.quantity + other.price * other.quantity

    @classmethod
    def new_product(cls, params: dict, products: list = None):
        return cls(params["name"], params["description"], params["price"], params["quantity"])

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, cost):
        if cost > 0:
            self.__price = cost
        else:
            print("Цена не должна быть нулевая или отрицательная")


class Category:
    name: str
    description: str
    __products: list
    category_count: int = 0
    product_count: int = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products
        self.category_count += len(products)
        self.product_count += sum(p.quantity for p in self.__products)

    def __str__(self):
        return f"{self.name}, количество продуктов: {self.product_count} шт."

    def add_product(self, prod: Product):
        self.__products.append(prod)
        self.product_count += 1

    @property
    def products(self):
        prods = ""
        for p in self.__products:
            prods += f"{p}\n"
        return prods


def create_obj_from_json(path: str) -> Category:
    try:
        with open(path, encoding='utf-8') as f:
            category_json = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        logger.warning(f'Something went wrong with {path}')
    for cat in category_json:
        prod = [Product(p['name'], p['description'], p['price'], p['quantity']) for p in cat['products']]
        category = Category(cat['name'], cat['description'], prod)
        yield category


if __name__ == '__main__':
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    print(str(product1))
    print(str(product2))
    print(str(product3))

    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3]
    )

    print(str(category1))

    print(category1.products)

    print(product1 + product2)
    print(product1 + product3)
    print(product2 + product3)