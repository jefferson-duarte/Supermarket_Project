from time import sleep

from controller.controller_supplier import ControllerSupplier
from utils import clean_screen


def supplier_view():
    supplier = ControllerSupplier()

    while True:
        clean_screen()
        print('=' * 35)
        print(f'{" Supplier ": ^35}')

        option_supplier = int(input(
            '===================================\n'
            '[1] Register a new supplier\n'
            '[2] Remove a supplier\n'
            '[3] Update a supplier\n'
            '[4] Show all suppliers\n'
            '[5] Exit\n'
            '===================================\n'
        ))

        match option_supplier:
            case 1:
                clean_screen()
                name = input('Insert the supplier name: ')
                cnpj = input('Insert the supplier CNPJ: ')
                phone = input('Insert the supplier phone: ')
                category = input('Insert the supplier category: ')

                supplier.register_supplier(
                    name, cnpj, phone, category
                )
                sleep(5)

            case 2:
                clean_screen()
                name = input(
                    'Insert the supplier name to remove: '
                )
                supplier.remove_supplier(name)
                sleep(5)

            case 3:
                clean_screen()
                old_name = input(
                    'Insert the supplier name to change: '
                )
                new_name = input('Insert the new supplier name: ')
                new_cnpj = input('Insert the cnpj: ')
                new_phone = input('Insert the phone: ')
                new_category = input('Insert the category: ')

                supplier.update_supplier(
                    old_name, new_name, new_cnpj, new_phone, new_category  # noqa:E501
                )
                sleep(5)

            case 4:
                clean_screen()
                supplier.show_suppiers()
                sleep(5)

            case 5:
                break
