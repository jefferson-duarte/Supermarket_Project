from dao import DaoCategory, DaoStock
from database_files import category_txt, stock_txt
from model import Category, Product, Stock


class ControllerCategory:
    def register_category(self, new_category: str):
        exist = False
        category_read = DaoCategory.read()

        for item in category_read:
            if item.category == new_category.title():
                exist = True

        if not exist:
            DaoCategory.save(new_category.title())
            print(f'Category "{new_category.title()}" registered successfully')
        else:
            print(f'Category "{new_category.title()}" already exist.')

    def remove_category(self, del_category: str):
        category = DaoCategory.read()
        filtered_category = list(
            filter(
                lambda item: item.category == del_category.title(), category
            )
        )

        if len(filtered_category) <= 0:
            print(f'Category "{del_category.title()}" does not exist.')

        else:
            for item in range(len(category)):
                if category[item].category == del_category.title():
                    del category[item]
                    break

            print(f'Category "{del_category.title()}" removed successfully.')

            try:
                with open(category_txt, 'w', encoding='utf-8') as file:
                    for item in category:
                        file.writelines(item.category)
                        file.writelines('\n')

            except Exception as e:
                print(f'Error: {e}')

    def update_category(self, old_category, new_category):
        category = DaoCategory.read()
        old_filtered_category = list(
            filter(lambda x: x.category == old_category, category)
        )

        if len(old_filtered_category) > 0:
            new_filtered_category = list(
                filter(lambda x: x.category == new_category, category)
            )

            if len(new_filtered_category) == 0:
                category = list(
                    map(
                        lambda x: Category(new_category)
                        if (x.category == old_category)
                        else (x),
                        category
                    )
                )
                print(
                    f'Category "{new_category}" updated successfully.'
                )
            else:
                print(f'Category "{new_category}" already exist.')

        else:
            print(f'Category "{old_category}" does not exist.')

        try:
            with open(category_txt, 'w', encoding='utf-8') as file:
                for item in category:
                    file.writelines(item.category)
                    file.writelines('\n')

        except Exception as e:
            print(f'Error: {e}')

    def show_category(self):
        categories = DaoCategory.read()

        if len(categories) == 0:
            print('No categories to show.')

        else:
            for category in categories:
                print(f'Category: {category.category}')


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
