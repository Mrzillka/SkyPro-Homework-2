import pytest

from main import *


@pytest.fixture()
def smartphone_products_as_products():
    p1 = Product("Samsung Galaxy S23 Ultra",
                 "256GB, Серый цвет, 200MP камера",
                 180000.0,
                 5)
    p2 = Product("Iphone 15",
                 "512GB, Gray space",
                 210000.0,
                 8)
    p3 = Product("Xiaomi Redmi Note 11",
                 "1024GB, Синий",
                 31000.0,
                 14)

    return [p1, p2, p3]


@pytest.fixture()
def smartphone_products_as_smartphones():
    s1 = Smartphone("Samsung Galaxy S23 Ultra",
                    "256GB, Серый цвет, 200MP камера",
                    180000.0,
                    5,
                    95.5,
                    "S23 Ultra",
                    256,
                    "Серый")
    s2 = Smartphone("Iphone 15",
                    "512GB, Gray space",
                    210000.0,
                    8,
                    98.2,
                    "15",
                    512,
                    "Gray space")
    s3 = Smartphone("Xiaomi Redmi Note 11",
                    "1024GB, Синий",
                    31000.0,
                    14,
                    90.3,
                    "Note 11",
                    1024,
                    "Синий")

    return [s1, s2, s3]


@pytest.fixture()
def tv_product():
    return Product("55\" QLED 4K",
                   "Фоновая подсветка",
                   123000.0,
                   7)


@pytest.fixture()
def grass_product():
    return LawnGrass("Nice Grass",
                     "This simply a nice grass",
                     1000,
                     17,
                     "Russia",
                     "17 days",
                     "white")


@pytest.fixture()
def category(smartphone_products_as_products):
    return Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        smartphone_products_as_products)


def test_product(tv_product):
    assert tv_product.name == "55\" QLED 4K"
    assert tv_product.description == "Фоновая подсветка"
    assert tv_product.price == 123000.0
    assert tv_product.quantity == 7
    new_product = Product.new_product(
        {
            "name": "Samsung Galaxy S23 Ultra",
            "description": "256GB, Серый цвет, 200MP камера",
            "price": 180000.0,
            "quantity": 5
        }
    )
    assert new_product.name == "Samsung Galaxy S23 Ultra"
    assert new_product.description == "256GB, Серый цвет, 200MP камера"
    assert new_product.price == 180000.0
    assert new_product.quantity == 5
    new_product.price = 800
    assert new_product.price == 800
    new_product.price = -1
    assert new_product.price == 800
    assert tv_product + new_product, 123000.0 * 7 + 800 * 5


def test_smartphone(smartphone_products_as_smartphones):
    s1, s2, s3 = smartphone_products_as_smartphones
    assert s1.name == "Samsung Galaxy S23 Ultra"
    assert s1.description == "256GB, Серый цвет, 200MP камера"
    assert s1.price == 180000.0
    assert s1.quantity == 5
    assert s1.efficiency == 95.5
    assert s1.model == "S23 Ultra"
    assert s1.memory == 256
    assert s1.color == "Серый"

    new_smartphone = Smartphone.new_product(
        {
            "name": "Xiaomi Redmi Note 11",
            "description": "1024GB, Синий",
            "price": 31000.0,
            "quantity": 14,
            "efficiency": 90.3,
            "model": "Note 11",
            "memory": 1024,
            "color": "Синий",
        }
    )
    assert new_smartphone.name == "Xiaomi Redmi Note 11"
    assert new_smartphone.description == "1024GB, Синий"
    assert new_smartphone.price == 31000.0
    assert new_smartphone.quantity == 14
    assert new_smartphone.efficiency == 90.3
    assert new_smartphone.model == "Note 11"
    assert new_smartphone.memory == 1024
    assert new_smartphone.color == "Синий"

    new_smartphone.price = 800
    assert new_smartphone.price == 800
    new_smartphone.price = -1
    assert new_smartphone.price == 800

    assert s1 + new_smartphone == 180000.0 * 5 + 800 * 14


def test_grass(grass_product):
    assert grass_product.name == "Nice Grass"
    assert grass_product.description == "This simply a nice grass"
    assert grass_product.price == 1000.0
    assert grass_product.quantity == 17
    assert grass_product.country == "Russia"
    assert grass_product.germination_period == "17 days"
    assert grass_product.color == "white"


    new_grass = LawnGrass.new_product(
        {
            "name": "Bad Grass",
            "description": "Not a very good grass",
            "price": 999.99,
            "quantity": 99,
            "country": "Sahara",
            "germination_period": "99 days",
            "color": "black",
        }
    )
    assert new_grass.name == "Bad Grass"
    assert new_grass.description == "Not a very good grass"
    assert new_grass.price == 999.99
    assert new_grass.quantity == 99
    assert new_grass.country == "Sahara"
    assert new_grass.germination_period == "99 days"
    assert new_grass.color == "black"

    new_grass.price = 800
    assert new_grass.price == 800
    new_grass.price = -1
    assert new_grass.price == 800

    assert grass_product + new_grass == 1000.0 * 17 + 800 * 99


def test_products_sum(smartphone_products_as_smartphones, tv_product):
    assert smartphone_products_as_smartphones[0] + smartphone_products_as_smartphones[2] == 180000.0 * 5 + 31000 * 14

    with pytest.raises(TypeError):
        smartphone_products_as_smartphones[0] + tv_product


def test_category(category, smartphone_products_as_products, tv_product):
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
    with pytest.raises(TypeError):
        category.add_product("Not a product")


def test_create_obj_from_json():
    assert list(create_obj_from_json("Not_a_path.json")) == []
    for obj in create_obj_from_json("data/products.json"):
        assert str(obj) in ("Смартфоны, количество продуктов: 27 шт.", "Телевизоры, количество продуктов: 7 шт.")


def test_category_iterator(category):
    lst = []
    for prod in CategoryIterator(category):
        lst.append(prod)
    assert lst == ["Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт.",
                   "Iphone 15, 210000.0 руб. Остаток: 8 шт.",
                   "Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт."]

def test_product_zero_quantity():
    with pytest.raises(ValueError):
        Product("...", "...", "...", 0)
