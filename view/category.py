import os

from controller.controller_category import ControllerCategory


def category_view():
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

        enter = True
        match option_category:
            case 1:
                while enter:
                    os.system('cls')
                    new_category = input(
                        'Insert a category to register: '
                    )
                    category.register_category(new_category)
                    exit = input('Type exit to close: ')

                    if exit:
                        enter = False
            case 2:
                while enter:
                    os.system('cls')
                    remove_category = input(
                        'Insert a category name to remove: '
                    )
                    category.remove_category(remove_category)

                    exit = input('Type exit to close: ')
                    if exit:
                        enter = False

            case 3:
                while enter:
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

                    exit = input('Type exit to close: ')
                    if exit:
                        enter = False
            case 4:
                while enter:
                    os.system('cls')
                    category.show_category()

                    exit = input('Type exit to close: ')
                    if exit:
                        enter = False
            case 5:
                break
