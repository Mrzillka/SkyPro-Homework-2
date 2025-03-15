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
    new_product = Product.new_product(
        {"name": "Samsung Galaxy S23 Ultra", "description": "256GB, Серый цвет, 200MP камера", "price": 180000.0,
         "quantity": 5})
    assert new_product.name == "Samsung Galaxy S23 Ultra"
    assert new_product.description == "256GB, Серый цвет, 200MP камера"
    assert new_product.price == 180000.0
    assert new_product.quantity == 5
    new_product.price = 800
    assert new_product.price == 800


def test_category(category, smartphone_products, tv_product):
    assert category.name == "Смартфоны"
    assert category.description == "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни"
    assert category.products == """Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт.
Iphone 15, 210000.0 руб. Остаток: 8 шт.
Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт.
"""
    assert category.category_count == 3
    assert category.product_count == 5 + 8 + 14
    category.add_product(tv_product)
    assert category.products == """Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт.
Iphone 15, 210000.0 руб. Остаток: 8 шт.
Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт.
55" QLED 4K, 123000.0 руб. Остаток: 7 шт.
"""
