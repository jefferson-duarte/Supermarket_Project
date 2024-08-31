from database_files import create_files
from utils import clean_screen
from view.category import category_view
from view.clients import client_view
from view.stock import stock_view
from view.supplier import supplier_view

if __name__ == '__main__':

    create_files()

    while True:
        clean_screen()

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
                category_view()
            case 2:
                stock_view()
            case 3:
                supplier_view()
            case 4:
                client_view()
            case 8:
                break
