from time import sleep

from controller.controller_employee import ControllerEmployee
from utils import clean_screen


def employee_view():
    employee = ControllerEmployee()

    while True:
        clean_screen()

        print('=' * 35)
        print(f'{" Employee ": ^35}')

        option_employee = int(input(
            '===================================\n'
            '[1] Register a new employee\n'
            '[2] Remove a employee\n'
            '[3] Update a employee\n'
            '[4] Show all employee\n'
            '[5] Exit\n'
            '===================================\n'
        ))

        match option_employee:
            case 1:
                clean_screen()

                name = input('Input the employee name: ')
                phone = input('Input the employee phone: ')
                email = input('Input the employee email: ')
                address = input('Input the employee address: ')
                cpf = input('Input the employee cpf: ')
                clt = input('Input the employee clt: ')

                employee.register_employee(
                    clt, name, phone, cpf, email, address
                )
                sleep(5)

            case 2:
                clean_screen()
                name = input('Input a name to remove: ')
                employee.remove_employee(name)
                sleep(5)

            case 3:
                old_name = input('Input the name to update: ')
                new_name = input('Input the new name: ')
                new_phone = input('Input the phone: ')
                new_email = input('Input the email: ')
                new_address = input('Input the address: ')
                new_cpf = input('Input the cpf: ')
                new_clt = input('Input the clt: ')

                employee.update_employee(
                    old_name, new_clt, new_name, new_phone, new_cpf, new_email, new_address  # noqa:E501
                )
                sleep(5)

            case 4:
                clean_screen()
                employee.show_employee()
                sleep(5)

            case 5:
                break
