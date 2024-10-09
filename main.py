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
        return f"{self.name}, {self.description}, {self.__products}"

    def add_product(self, prod: Product):
        self.__products.append(prod)

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


if __name__ == "__main__":
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3]
    )

    print(category1.products)
    product4 = Product("55\" QLED 4K", "Фоновая подсветка", 123000.0, 7)
    category1.add_product(product4)
    print(category1.products)
    print(category1.product_count)

    new_product = Product.new_product(
        {"name": "Samsung Galaxy S23 Ultra", "description": "256GB, Серый цвет, 200MP камера", "price": 180000.0,
         "quantity": 5})
    print(new_product.name)
    print(new_product.description)
    print(new_product.price)
    print(new_product.quantity)

    new_product.price = 800
    print(new_product.price)

    new_product.price = -100
    print(new_product.price)
    new_product.price = 0
    print(new_product.price)
