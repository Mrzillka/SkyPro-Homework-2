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
        self.price = price
        self.quantity = quantity


class Category:
    name: str
    description: str
    products: list
    category_count: int = 0
    product_count: int = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.products = products
        self.category_count += len(products)
        self.product_count += sum(p.quantity for p in self.products)

    def __str__(self):
        return f"{self.name}, {self.description}, {self.products}"


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

    print(product1.name)
    print(product1.description)
    print(product1.price)
    print(product1.quantity)

    print(product2.name)
    print(product2.description)
    print(product2.price)
    print(product2.quantity)

    print(product3.name)
    print(product3.description)
    print(product3.price)
    print(product3.quantity)

    category1 = Category("Смартфоны",
                         "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
                         [product1, product2, product3])

    print(category1.name == "Смартфоны")
    print(category1.description)
    print(len(category1.products))
    print(category1.category_count)
    print(category1.product_count)

    product4 = Product("55\" QLED 4K", "Фоновая подсветка", 123000.0, 7)
    category2 = Category(
        "Телевизоры",

        "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
        [product4]
    )

    print(category2.name)
    print(category2.description)
    print(len(category2.products))
    print(category2.products)

    print(Category.category_count)
    print(Category.product_count)
