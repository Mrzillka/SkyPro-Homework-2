import pytest

from main import *


@pytest.fixture()
def smartphone_products():
    return [Product("Samsung Galaxy S23 Ultra",
                    "256GB, Серый цвет, 200MP камера",
                    180000.0,
                    5),
            Product("Iphone 15",
                    "512GB, Gray space",
                    210000.0,
                    8),
            Product("Xiaomi Redmi Note 11",
                    "1024GB, Синий",
                    31000.0,
                    14)]


@pytest.fixture()
def tv_product():
    return Product("55\" QLED 4K",
                   "Фоновая подсветка",
                   123000.0,
                   7)


@pytest.fixture()
def category(smartphone_products):
    return Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        smartphone_products)


def test_product(tv_product):
    assert tv_product.name == "55\" QLED 4K"
    assert tv_product.description == "Фоновая подсветка"
    assert tv_product.price == 123000.0
    assert tv_product.quantity == 7


def test_category(category, smartphone_products):
    assert category.name == "Смартфоны"
    assert category.description == "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни"
    assert category.products == smartphone_products
    assert category.category_count == 3
    assert category.product_count == 5 + 8 + 14
