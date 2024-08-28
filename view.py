import os
from time import sleep

from controller.controller_category import ControllerCategory
from controller.controller_client import ControllerClient
from controller.controller_sale import ControllerSale
from controller.controller_stock import ControllerStock
from controller.controller_supplier import ControllerSupplier
from database_files import create_files

if __name__ == '__main__':

    create_files()

    while True:
        os.system('cls')

        print('~' * 35)
        print(f'{" SUPERMARKET ": ^35}')
        print('~' * 35)

        main_menu = int(input(
            '[1] Categories\n'
            '[2] Stock\n'
            '[3] Supplier\n'
            '[4] Clients\n'
            '[5] Employees\n'
            '[6] Sell\n'
            '[7] Best Selling Products\n'
            '[8] Exit\n'
            '===================================\n'
        ))

        match main_menu:
            case 1:
                category = ControllerCategory()
                while True:
                    os.system('cls')
                    print('=' * 35)
                    print(f'{" Category ": ^35}')

                    option_category = int(input(
                        '===================================\n'
                        '[1] Register a new category\n'
                        '[2] Remove a category\n'
                        '[3] Update a category\n'
                        '[4] Show all categories\n'
                        '[5] Exit\n'
                        '===================================\n'
                    ))

                    match option_category:
                        case 1:
                            os.system('cls')
                            new_category = input(
                                'Insert a category to register: '
                            )
                            category.register_category(new_category)
                            sleep(3)
                        case 2:
                            os.system('cls')
                            remove_category = input(
                                'Insert a category name to remove: '
                            )
                            category.remove_category(remove_category)
                        case 3:
                            os.system('cls')
                            old_category = input(
                                'Insert the category name to update: '
                            )
                            new_category = input(
                                'Isert the new category name: '
                            )
                            category.update_category(
                                old_category, new_category
                            )
                        case 4:
                            os.system('cls')
                            category.show_category()
                            sleep(5)
                        case 5:
                            break

            case 2:
                stock = ControllerStock()
                while True:
                    os.system('cls')
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
                            os.system('cls')
                            name = input('Insert the product name: ')
                            price = input('Insert the product price: ')
                            category = input('Insert the product category: ')
                            quantity = input('Insert the product quantity: ')

                            stock.register_product(
                                name, price, category, quantity
                            )
                            sleep(5)

                        case 2:
                            os.system('cls')
                            name = input('Insert the product name to remove: ')
                            stock.remove_product(name)
                            sleep(5)

                        case 3:
                            os.system('cls')
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
                            os.system('cls')
                            stock.show_stock()
                            sleep(5)

                        case 5:
                            break

            case 8:
                break
