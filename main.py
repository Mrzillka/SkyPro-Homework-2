import json
import logging
from abc import ABC, abstractmethod
from typing import Any, Generator

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(module)s %(levelname)s: %(message)s',
                    filename=r'logs/main_logs.log',
                    filemode='w')
logger = logging.getLogger(__name__)

logger.info("Using module main")


class MixinPrintOnCreate:
    def __init__(self, cls):
        print(cls.__repr__())


class BaseProduct(ABC):

    @classmethod
    @abstractmethod
    def new_product(cls, params):
        pass

    @abstractmethod
    def price(self):
        pass


class Product(MixinPrintOnCreate, BaseProduct):
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
        if not quantity:
            raise ValueError("Товар с нулевым количеством не может быть добавлен")
        super().__init__(self)

    def __str__(self):
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    def __repr__(self):
        return f"{self.__class__.__name__}({self.name}, {self.__price}, {self.quantity})"

    def __add__(self, other):
        if type(other) == self.__class__:
            return self.__price * self.quantity + other.price * other.quantity
        raise TypeError

    @classmethod
    def new_product(cls, params: dict):
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
        if not isinstance(prod, Product):
            raise TypeError
        self.__products.append(prod)
        self.product_count += 1

    @property
    def products(self):
        prods = ""
        for p in self.__products:
            prods += f"{p}\n"
        return prods

    def middle_price(self):
        summa = sum(product.price for product in self.__products)
        try:
            return summa / self.product_count
        except ZeroDivisionError:
            return 0



class Smartphone(Product):
    efficiency: float
    model: str
    memory: int
    color: str

    def __init__(self, name, description, price, quantity, efficiency, model, memory, color):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

    @classmethod
    def new_product(cls, params: dict):
        return cls(params["name"],
                   params["description"],
                   params["price"],
                   params["quantity"],
                   params["efficiency"],
                   params["model"],
                   params["memory"],
                   params["color"])


class LawnGrass(Product):
    country: str
    germination_period: str
    color: str

    def __init__(self, name, description, price, quantity, country, germination_period, color):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

    @classmethod
    def new_product(cls, params: dict):
        return cls(params["name"],
                   params["description"],
                   params["price"],
                   params["quantity"],
                   params["country"],
                   params["germination_period"],
                   params["color"])


class CategoryIterator:
    def __init__(self, category):
        self.category = category

    def __iter__(self):
        self.product_number = -1
        return self

    def __next__(self):
        if self.product_number + 1 < len(self.category.products.split("\n")) - 1:
            self.product_number += 1
            return self.category.products.split("\n")[self.product_number]
        else:
            raise StopIteration


def create_obj_from_json(path: str) -> Generator[Category, Any, None]:
    """
    Creates a generator using a json file

    :param path: any str
    :return: Generator object
    """
    try:
        with open(path, encoding='utf-8') as f:
            category_json = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        logger.warning(f'Something went wrong with {path}')
        return
    for cat in category_json:
        prod = [Product(p['name'], p['description'], p['price'], p['quantity']) for p in cat['products']]
        category = Category(cat['name'], cat['description'], prod)
        yield category


if __name__ == '__main__':
    try:
        product_invalid = Product("Бракованный товар", "Неверное количество", 1000.0, 0)
    except ValueError as e:
        print(
            "Возникла ошибка ValueError прерывающая работу программы при попытке добавить продукт с нулевым количеством")
    else:
        print("Не возникла ошибка ValueError при попытке добавить продукт с нулевым количеством")

    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    category1 = Category("Смартфоны", "Категория смартфонов", [product1, product2, product3])

    print(category1.middle_price())

    category_empty = Category("Пустая категория", "Категория без продуктов", [])
    print(category_empty.middle_price())
