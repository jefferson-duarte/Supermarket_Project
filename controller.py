from datetime import datetime

from dao import DaoCategory, DaoSell, DaoStock
from database_files import category_txt, stock_txt
from model import Category, Product, Sell, Stock


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


class ControllerSale:
    def register_sale(self, product_name, seller, customer, quantity_sold):
        dao_stock = DaoStock.read()
        temp = []
        exist = False
        quantity = False

        for item in dao_stock:
            if not exist:
                if item.product.name == product_name:
                    exist = True
                    if item.quantity >= quantity_sold:
                        quantity = True
                        item.quantity = int(item.quantity) - int(quantity_sold)

                        sold = Sell(
                            Product(item.product.name, item.product.price, item.product.category),  # noqa:E501
                            seller, customer, quantity_sold
                        )

                        purchase_value = int(
                            quantity_sold) * int(item.product.price)

                        DaoSell.save(sold)

            temp.append(
                [Product(item.product.name, item.product.price, item.product.category), item.quantity]  # noqa:E501
            )

        file = open(stock_txt, 'w', encoding='utf-8')
        file.write('')
        file.close()

        for item in temp:
            with open(stock_txt, 'a', encoding='utf-8') as file:
                file.writelines(f'{item[0].name}|{item[0].price}|{item[0].category}|{item[1]}')  # noqa:E501
                file.writelines('\n')

        if not exist:
            print(f'Product "{product_name}" does not exist.')
            return None
        elif not quantity:
            print(f'Quantity "{quantity_sold}" not avaliable in stock.')
            return None
        else:
            print(f'Product "{product_name}" sold successfully.')
            return purchase_value

    def products_report(self):
        dao_sell = DaoSell.read()
        products = []

        for item in dao_sell:
            name = item.itens_sold.name
            quantity = item.quantity_sold
            length = list(filter(lambda x: x['product'] == name, products))

            if len(length) > 0:
                products = list(
                    map(
                        lambda x: {'product': name, 'quantity': int(x['quantity']) + int(quantity)}  # noqa:E501
                        if (x['product'] == name)
                        else (x), products
                    )
                )

            else:
                products.append({'product': name, 'quantity': int(quantity)})

        ordened = sorted(
            products, key=lambda k: k['quantity'], reverse=True
        )

        print('~' * 30)
        print(f'{"Best Selling Products": ^30}')
        print('~' * 30)
        cont = 1

        for item in ordened:
            print(f'{f" Product {cont} ":=^30}')
            print(
                f'Product: {item['product']}\n'
                f'Quantity: {item['quantity']}\n'
            )
            cont += 1

    def show_sales(self, date_start, date_last):
        dao_sell = DaoSell.read()

        date_start = datetime.strptime(date_start, '%d/%m/%Y')
        date_last = datetime.strptime(date_last, '%d/%m/%Y')

        selected_sales = list(
            filter(
                lambda x: datetime.strptime(x.data, '%d/%m/%Y') >= date_start
                and datetime.strptime(x.data, '%d/%m/%Y') <= date_last, dao_sell  # noqa:E501
            )
        )

        cont = 1
        total = 0

        for item in selected_sales:
            print(f'{f" Sales [{cont}] ":=^30}')
            print(
                f'Name......: {item.itens_sold.name}\n'
                f'Category..: {item.itens_sold.category}\n'
                f'Date......: {item.data}\n'
                f'Quantity..: {item.quantity_sold}\n'
                f'Customer..: {item.customer}\n'
                f'Saller....: {item.seller}\n'
            )
            total += int(item.itens_sold.price) * int(item.quantity_sold)
            cont += 1

        print(f'Total sold: €{total:.2f}')


sale = ControllerSale()
# sale.products_report()
sale.show_sales('25/08/2024', '25/08/2024')
