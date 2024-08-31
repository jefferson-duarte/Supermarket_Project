from time import sleep

from controller.controller_stock import ControllerStock
from utils import clean_screen


def stock_view():
    stock = ControllerStock()

    while True:
        clean_screen()
        print('=' * 35)
        print(f'{" Stock ": ^35}')

        option_stock = int(input(
            '===================================\n'
            '[1] Register a new product\n'
            '[2] Remove a product\n'
            '[3] Update a product\n'
            '[4] Show all products\n'
            '[5] Exit\n'
            '===================================\n'
        ))

        match option_stock:
            case 1:
                clean_screen()
                name = input('Insert the product name: ')
                price = input('Insert the product price: ')
                category = input('Insert the product category: ')
                quantity = input('Insert the product quantity: ')

                stock.register_product(
                    name, price, category, quantity
                )
                sleep(5)

            case 2:
                clean_screen()
                name = input('Insert the product name to remove: ')
                stock.remove_product(name)
                sleep(5)

            case 3:
                clean_screen()
                update_name = input(
                    'Insert the product name to change: '
                )
                new_name = input('Insert the new product name: ')
                new_price = input('Insert the price: ')
                new_category = input('Insert the category: ')
                new_quantity = input('Insert the quantity: ')

                stock.update_product(
                    update_name, new_name, new_price, new_category, new_quantity  # noqa:E501
                )
                sleep(5)

            case 4:
                clean_screen()
                stock.show_stock()
                sleep(5)

            case 5:
                break
