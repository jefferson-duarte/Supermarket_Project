from time import sleep

from controller.controller_category import ControllerCategory
from utils import clean_screen


def category_view():
    category = ControllerCategory()
    while True:
        clean_screen()

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
                clean_screen()
                new_category = input(
                    'Insert a category to register: '
                )
                category.register_category(new_category)
                sleep(5)
            case 2:
                clean_screen()
                remove_category = input(
                    'Insert a category name to remove: '
                )
                category.remove_category(remove_category)
                sleep(5)

            case 3:
                clean_screen()
                old_category = input(
                    'Insert the category name to update: '
                )
                new_category = input(
                    'Isert the new category name: '
                )
                category.update_category(
                    old_category, new_category
                )
                sleep(5)

            case 4:
                clean_screen()
                category.show_category()
                sleep(5)

            case 5:
                break
