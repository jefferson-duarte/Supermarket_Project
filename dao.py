import os
from pathlib import Path

from model import Category, Product, Sell

BASE_DIR = Path(__file__).parent
category_txt = os.path.join(BASE_DIR, 'database/category.txt')
sell_txt = os.path.join(BASE_DIR, 'database/sell.txt')


class DaoCategory:
    @classmethod
    def save(cls, category):
        with open(category_txt, 'a', encoding='utf-8') as file:
            file.writelines(category)
            file.writelines('\n')

    @classmethod
    def read(cls):
        with open(category_txt, 'r', encoding='utf-8') as file:
            cls.category = file.readlines()

        cls.category = list(map(lambda x: x.replace('\n', ''), cls.category))

        list_categories = []
        for item in cls.category:
            list_categories.append(Category(item))

        return list_categories


class DaoSell:
    @classmethod
    def save(cls, sell: Sell):
        with open(sell_txt, 'a', encoding='utf-8') as file:
            file.writelines(
                f'{sell.itens_sold.name} | {sell.itens_sold.price} | '
                f'{sell.itens_sold.category} | {sell.seller} | '
                f'{sell.customer} | {sell.quantity_sold} | {sell.data}'
            )
            file.writelines('\n')

    @classmethod
    def read(cls):
        with open(sell_txt, 'r', encoding='utf-8') as file:
            cls.sell = file.readlines()

        cls.sell = list(map(lambda x: x.replace('\n', ''), cls.sell))
        cls.sell = list(map(lambda x: x.split('|'), cls.sell))

        list_sell = []
        for item in cls.sell:
            list_sell.append(
                Sell(
                    Product(item[0], item[1], item[2]),
                    item[3], item[4], item[5], item[6]
                )
            )

        return list_sell
