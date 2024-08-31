from time import sleep

from controller.controller_sale import ControllerSale
from utils import clean_screen


def best_products():
    sale = ControllerSale()

    while True:
        clean_screen()

        print('=' * 35)
        print(f'{" Best Selling Products ": ^35}')

        option_sale = int(input(
            '===================================\n'
            '[1] Show the best products\n'
            '[2] Exit\n'
            '===================================\n'
        ))

        match option_sale:
            case 1:
                clean_screen()
                sale.products_report()
                sleep(5)

            case 2:
                break
