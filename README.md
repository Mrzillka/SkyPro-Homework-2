# SkyPro HomeWork 3

## Описание

Здесь хранятся файлы для домашних заданий в курсе SkyPro Профессия Python-разработчик.

Блок 4 Объектно-ориентированное программирование

## Установка

1. Клонируйте репозиторий:
    ```
    git clone https://github.com/Mrzillka/SkyPro-Homework-2.git
    ```

## Использование:

- Запустите файл `main.py`

### Тестирование
Запустите команду `pytest` в консоли

## Документация:

### `main.py`

- `class Product`
- - `name: str`
- - `description: str`
- - `price: float`
- - `quantity: int`


- `class Smartphone(Product)`
- - `efficiency: float`
- - `model: str`
- - `memory: int`
- - `color: str`


- `class LawnGrass(Product)`
- - `country: str`
- - `germination_period: str`
- - `color: str`


- `class Category`
- - `name: str`
- - `description: str`
- - `products: list`
- - `category_count: int`
- - `product_count: int`


- `class CategoryIterator`


- `def create_obj_from_json(path)`
- - "Creates a generator using a json file"