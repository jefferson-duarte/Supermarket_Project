from datetime import datetime

from dao import DaoSell, DaoStock
from database_files import stock_txt
from model import Product, Sell


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
                    if item.quantity >= int(quantity_sold):
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
