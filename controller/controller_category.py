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

        dao_stock = DaoStock.read()

        stock = list(
            map(
                lambda x: Stock(
                    Product(x.product.name, x.product.price, 'No Category'), x.quantity  # noqa:E501
                )
                if (x.product.category == del_category)
                else (x), dao_stock
            )
        )

        with open(stock_txt, 'w', encoding='utf-8') as file:
            for item in stock:
                file.writelines(
                    f'{item.product.name}|{item.product.price}|'
                    f'{item.product.category}|{item.quantity}'
                )
                file.writelines('\n')

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

                dao_stock = DaoStock.read()

                stock = list(
                    map(
                        lambda x: Stock(
                            Product(x.product.name, x.product.price, new_category), x.quantity  # noqa:E501
                        )
                        if (x.product.category == old_category)
                        else (x), dao_stock
                    )
                )

                with open(stock_txt, 'w', encoding='utf-8') as file:
                    for item in stock:
                        file.writelines(
                            f'{item.product.name}|{item.product.price}|'
                            f'{item.product.category}|{item.quantity}'
                        )
                        file.writelines('\n')

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
