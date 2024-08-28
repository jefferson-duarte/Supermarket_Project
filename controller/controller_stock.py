from dao import DaoCategory, DaoStock
from database_files import stock_txt
from model import Product, Stock


class ControllerStock:
    def register_product(self, name, price, category, quantity):
        dao_stock = DaoStock.read()
        dao_category = DaoCategory.read()

        filter_category = list(
            filter(lambda x: x.category == category, dao_category)
        )
        filter_stock = list(
            filter(lambda x: x.product.name == name, dao_stock)
        )

        if len(filter_category) > 0:
            if len(filter_stock) == 0:
                product = Product(name, price, category)
                DaoStock.save(product, quantity)
                print(f'Product "{product.name}" registed successfully')
            else:
                print(f'Product "{name}" already exist.')
        else:
            print(f'Category "{category}" does not exist.')

    def remove_product(self, name):
        dao_stock = DaoStock.read()
        filter_product = list(
            filter(lambda x: x.product.name == name, dao_stock)
        )

        if len(filter_product) > 0:
            for item in range(len(dao_stock)):
                if dao_stock[item].product.name == name:
                    del dao_stock[item]
                    break
            print(f'Product "{name}" removed successfully.')
        else:
            print(f'Product "{name}" does not exist.')

        with open(stock_txt, 'w', encoding='utf-8') as file:
            for item in dao_stock:
                file.writelines(
                    f'{item.product.name}|{item.product.price}|'
                    f'{item.product.category}|{item.quantity}'
                )
                file.writelines('\n')

    def update_product(self, update_name, new_name, new_price, new_category, new_quantity):  # noqa:E501
        dao_stock = DaoStock.read()
        dao_category = DaoCategory.read()
        filter_category = list(
            filter(lambda x: x.category == new_category, dao_category)
        )

        if len(filter_category) > 0:
            product_name = list(
                filter(lambda x: x.product.name == update_name, dao_stock)
            )
            if len(product_name) > 0:
                product_name = list(
                    filter(lambda x: x.product.name == new_name, dao_stock)
                )
                if len(product_name) == 0:
                    dao_stock = list(
                        map(
                            lambda x: Stock(
                                Product(new_name, new_price, new_category),
                                new_quantity
                            )
                            if (x.product.name == update_name)
                            else (x), dao_stock
                        )
                    )
                    print(f'Product "{new_name}" registed successfully.')
                else:
                    print(f'Produtc "{new_name}" already registed.')
            else:
                print(f'Product "{update_name}" does not exist.')

            with open(stock_txt, 'w', encoding='utf-8') as file:
                for item in dao_stock:
                    file.writelines(
                        f'{item.product.name}|{item.product.price}|'
                        f'{item.product.category}|{item.quantity}'
                    )
                    file.writelines('\n')

        else:
            print(f'Category "{new_category}" already exist.')

    def show_stock(self):
        dao_stock = DaoStock.read()

        if len(dao_stock) == 0:
            print('Stock empty.')
        else:
            print(f'{"[Products]":#^30}')
            for item in dao_stock:
                print(
                    f'Name.......: {item.product.name}\n'
                    f'Price......: {item.product.price}\n'
                    f'Category...: {item.product.category}\n'
                    f'Quantity...: {item.quantity}'
                )
                print('-' * 30)
