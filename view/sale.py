from time import sleep

from controller.controller_sale import ControllerSale
from utils import clean_screen


def sale_view():
    sale = ControllerSale()

    while True:
        clean_screen()

        print('=' * 35)
        print(f'{" Sale ": ^35}')

        option_sale = int(input(
            '===================================\n'
            '[1] Register a new sale\n'
            '[2] Show all sales\n'
            '[3] Exit\n'
            '===================================\n'
        ))

        match option_sale:
            case 1:
                clean_screen()

                product_name = input('Input the product name: ')
                seller = input('Input the seller name: ')
                customer = input('Input the customer name: ')
                quantity_sold = input('Input the quantity sold: ')

                sale.register_sale(
                    product_name, seller, customer, quantity_sold
                )
                sleep(5)

            case 2:
                clean_screen()
                date_start = input('Input the start date: ')
                date_last = input('Input the last date: ')
                sale.show_sales(date_start, date_last)
                sleep(5)

            case 3:
                break
